
let current_usr = ""
let current_cid = undefined;
let current_chats = {}// cid: chat obj

let ws;
let dialog_div;

let signin_checkbox;
let signup_checkbox;
let joinchat_checkbox;

function assert(condition, message) {
    if (!condition) {
        message = message || "Assertion failed";
        if (typeof Error !== "undefined") {
            throw new Error(message);
        }
        throw message; // Fallback
    }
}
//execute function in server
function exec_server(exp) {
    console.log("exec server:", exp)
    data = {"api": "exec", "args": [exp]}
    ws.send(JSON.stringify(data))
}

function top_chat(cid) {
    console.log("top_chat", cid)
    //FIXME server side record timestamp
    let children = chatlists[0].children;
    for (let i = 0; i < children.length; i += 1) {
        if (children[i].cid === cid) {
            LM.collapse_list_set_top(children[i]);
            break;
        }
    }
}

class Msg {
    constructor(username, msg, time) {
        this.username = username;
        this.msg = msg;
        this.time = time;
    }
}

class Chat {
    constructor(cid, title, timestamp=new Date(0)) {
        this.cid = cid;
        this.msgs = [];
        this.title = title;
        this.timestamp = timestamp;
    }
    add_msg(msg) {

        this.msgs.push(msg);

        let d = new Date(msg.time);
        if (d > this.timestamp) {
            top_chat(this.cid);
            //TODO notification count style
            this.timestamp = d;
        }

        if (current_cid == this.cid) {
            //FIXME
            dialog_div.appendChild(create_msg_element(msg));
            this.ack_all();
        }
    }
    ack_all() {
        let last_time = new Date(this.msgs[this.msgs.length-1].time);
        last_time = last_time.getTime() / 1000;
        exec_server(`update_chat_timestamp(${this.cid}, ${last_time})`)
    }
    print() {
        console.log(this.cid, this.msgs);
    }
}

const time_msg_style = `
                        border: 1px solid rgba(0, 0, 0, .12);
                        background-color: rgba(0, 0, 0, .04);
                        color: rgba(0, 0, 0, .6);
                        align-self: center;
                        margin-bottom: 1em;`;

const user_msg_style = `border: 1px solid rgba(0, 0, 0, .12);
                        border-radius: 1em 1em 0 1em;
                        color: rgba(0, 0, 0, .8);
                        align-self: flex-end;
                        margin-bottom: 1em;`;

const other_msg_style = `border-radius: 1em 1em 1em 0em;
                         background-color: rgba(0, 0, 0, .8);
                         color: white;
                         align-self: flex-start;
                         margin-bottom: 1em;`;

function create_msg_element(msg) {

    let c = document.createElement("div");
    //time
    if (!msg.msg) {

        const now = new Date(Date.now())
        const this_date_str = now.toDateString().split(" ");
        const this_day = this_date_str[2]
        const this_month = this_date_str[1];
        const this_year = this_date_str[3];

        const date_str = msg.toDateString().split(" ");
        const day = date_str[2]
        const month = date_str[1];
        const year = date_str[3];

        const hour_minute = msg.toTimeString().split(":").slice(0, 2).join(":");
        let time_str = hour_minute;

        if (this_year == year && this_month == month && this_day == day) 
            time_str = "Today " + time_str;
        else if (this_year == year) 
            time_str = time_str + " " + month + " " + day;
        else 
            time_str = time_str + " " + month + " " + day + " " + year;

        c.className = "card--outlined";
        c.innerHTML = time_str;
        c.style = time_msg_style;
        return c;
    }
    c.className = "card--flat";
    c.innerHTML = msg.msg;
    if (msg.username == current_usr)
        c.style = user_msg_style;
    else 
        c.style = other_msg_style;
    return c;
}



let switch_chat_lock = 0;

//switch to chat, also update user's per-cid timestamp on the server side
//TODO 
function switch_chat(dialog_div, chat_obj) {
    if (chat_obj.cid == current_cid)
        return;

    if (switch_chat_lock) {
        //setTimeout(() => {switch_chat(dialog_div, chat_obj)}, 1000);
        //or abort?
        return;
    }

    else {
        switch_chat_lock = 1;
        dialog_div.classList.remove("reveal");
        dialog_div.style = `
            display: flex; flex-direction: column; align-items: flex-start; margin-top: 1.5em;
            opacity: 0;
            transition: opacity .2s;
        `;
        setTimeout(() => {

            //switch dialog items
            current_cid = chat_obj.cid
            //console.log("switch to: ", chat_obj)
            chat_obj.ack_all();
            top_chat(current_cid);

            dialog_div.innerHTML = "";

            let pre_insert_time = new Date(0);
            for (let i = 0; i < chat_obj.msgs.length; i ++) { 
                const time = new Date(chat_obj.msgs[i].time)
                const ds = (time - pre_insert_time)/1000; 
                if (ds > 10*60) {
                    pre_insert_time = time;
                    dialog_div.appendChild(create_msg_element(time))
                }
                dialog_div.appendChild(create_msg_element(chat_obj.msgs[i]));
            }

            dialog_div.classList.add("reveal");
            dialog_div.style = `
                display: flex; flex-direction: column; align-items: flex-start; margin-top: 1.5em;
                opacity: 1;
            `;
            setTimeout(() => { switch_chat_lock = 0 }, 200);
    
        }, 500);
    }
}


function add_msg(cid, user, msg, time) {

    if (switch_chat_lock) 
        setTimeout(() => {add_msg(cid, user, msg, time)}, 1000);
    else {
        if (current_chats[cid] === undefined) {
            console.log("Warning: add_msg: cid not in current chats");
            return;
        }
        current_chats[cid].add_msg(new Msg(user, msg, time));
    }
}


//API begin
valid_func = ["test_exec_client", 
              "recv_chat",
              "recv_msg",

              "signup_callback", 
              "signin_callback", 
              "join_chat_callback", 
              "send_msg_callback", 
              ]; 

function test_exec_client() {
    console.log("test success");
}

//callbacks from server
//should NOT call to server
function signup_callback(err, msg) {
    console.log(err, msg);
    if (err == 0) {
        signup_checkbox.checked = false;
    }
    else {
        LM.toast(msg)
    }
}

function signin_callback(err, msg) {
    console.log(err, msg);
    if (err == 0) {
        signin_checkbox.checked = false;
        LM.toast(`Welcome, ${current_usr}`)
    }
    else {
        LM.toast(msg)
    }
}

function join_chat_callback(err, msg) {
    console.log(err, msg);
    if (err == 0) {
        //chat is added by server, which will call recv_chat
        joinchat_checkbox.checked = false;
    }
    else {
        LM.toast(msg)
    }
}
function send_msg_callback(err, msg) {
    console.log(err, msg);
}



//NOTE recv_chat(cid...) must be called before this
//1. fetch old chat logs when login
//2. announced by other client
function recv_msg(cid, username, msg, time) {
    add_msg(cid, username, msg, time);
}

//NOTE the only way to create a new chat at fontend(by join chat or other user's notification)
function recv_chat(cid, title, time) {
    if (current_chats[cid] === undefined) {
        let c = new Chat(cid=cid, title=title, timestamp=new Date(time));
        current_chats[cid] = c;
        chatlists[0].add_chat(c);//add chat html element
        chatlists[1].add_chat(c);
    }
    else 
        console.log("Warn: recv duplicate chat info");
}

//API end

// Then we can control directly call function from server
// e.g. exec("a_global_func(args)")
function exec_client(exp) {
    exp = exp.trim()
    let i;
    for (i = 0; i < exp.length; i += 1) 
        if (exp[i] == "(") 
            break;
    const func = exp.substr(0, i).trim();

    if (!valid_func.includes(func)) {
        console.log("invalid function ", func);
        return;
    }

    let arg_string = "[" + exp.substr(i+1, exp.length - i-2) + "]";
    args = JSON.parse(arg_string);

    window[func](...args);
} 


function main() {

    //send
    send_input = document.getElementById("sendinput");
    send_btn = document.getElementById("sendbtn")
    send_btn.onclick = (e) => {
        send_msg = send_input.value;
        if (send_msg && current_cid) {
            exec_server(`send_msg(${current_cid}, "${send_msg}")`)
        }
        send_input.value = "";
    }
    send_input.onkeyup = (e) => {
        if (e.key == "Enter") 
            send_btn.click();
    };

    //recv and update global chats

    //where we display the chat history given chat_id
    dialog_div = document.getElementById("dialog");

    //Since we have both landscape and portrait chat list
    // each chat item is relative to a chat 
    chatlists = [];
    chatlists.push(document.getElementById("landscapechatlist"));
    chatlists.push(document.getElementById("portraitchatlist"));
    chatlists[0].add_chat = (chat_obj) => {

        //FIXME
        item = document.createElement("div");
            let c = document.createElement("div");
            c.className = "collapse-list-button";
            c.innerHTML = chat_obj.title;
            item.appendChild(c);

        item.className = "list-item--expand";
        item.cid = chat_obj.cid;
        item.onclick = (e) => {
            switch_chat(dialog_div, chat_obj);
        }
        chatlists[0].appendChild(item);

    }
    chatlists[1].add_chat = (chat_obj) => {
        //TODO portrait support
    
    }
    LM.collapse_list_init(chatlists[0], 1);


    // create new chat by chat key
    joinchat_checkbox = document.getElementById("addchat-dialog-trigger");
    joinchat_btn = document.getElementById("joinchatbtn");
    joinchat_input = document.getElementById("joinchatinput");
    joinchat_checkbox.onchange = (e) => {
        if(e.target.checked) 
            joinchat_input.focus();
    }
    joinchat_btn.onclick = (e) => {
        //LM.toast("This is a toast"); return;
        key = joinchat_input.value;
        if (key)
            exec_server(`join_chat("${key}")`)
        else {
            console.log("Please input key");
        }
    }
    joinchat_checkbox.nextElementSibling.tabIndex = "0";
    joinchat_checkbox.nextElementSibling.onkeyup = (e) => {
        if (e.key == "Escape")
            joinchat_checkbox.checked = false;
    };


    //TODO delete chat
    delchat_btn = document.getElementById("delchatbtn");

    //user management
    signin_name = document.getElementById("signinname");
    signin_pwd = document.getElementById("signinpwd");
    signin_checkbox = document.getElementById("signin-dialog-trigger");
    signin_checkbox.onchange = (e) => {
        if(e.target.checked) 
            signin_name.focus();
    }
    signin_checkbox.nextElementSibling.tabIndex = "0";
    signin_checkbox.nextElementSibling.onkeyup = (e) => {
        if (e.key == "Escape")
            signin_checkbox.checked = false;
    };

    signin_btn = document.getElementById("signinbtn");
    signin_btn.onclick = (e) => {
        if (current_usr) {
            LM.toast("You are already logged in.")
            return;
        }
        const username = signin_name.value;
        const pwd = signin_pwd.value;
        if (username && pwd) {
            exec_server(`signin("${username}", "${pwd}")`)
            current_usr = username;
        }
        else {
            console.log("null name or pwd");
        }
       
    }

    signin_checkbox.click()//show sign in dialog first

    signup_checkbox = document.getElementById("signup-dialog-trigger");
    signup_name = document.getElementById("signupname");
    signup_pwd = document.getElementById("signuppwd");
    signup_checkbox.onchange = (e) => {
        if(e.target.checked) 
            signup_name.focus();
    }
    signup_btn = document.getElementById("signupbtn");
    signup_btn.onclick = (e) => {

        const username = signup_name.value;
        const pwd = signup_pwd.value;
        if (username && pwd) 
            exec_server(`signup("${username}", "${pwd}")`)
        else {
            console.log("null name or pwd");
        }
    }
    signup_checkbox.nextElementSibling.tabIndex = "0";
    signup_checkbox.nextElementSibling.onkeyup = (e) => {
        if (e.key == "Escape")
            signup_checkbox.checked = false;
    };

    function start_ws() {
    
        ws = new WebSocket("ws://localhost:8081/");
        console.log("start ws");
        ws.onopen = (e) => {
            console.log("websock connected");
            exec_server("test_exec_server()");
        }
        ws.onmessage = (e) => {
            //console.log(`recv: ${e.data}`);
            data = JSON.parse(e.data)
            if (data["api"] === "exec") 
                exec_client(data["args"][0]);
        }
        ws.onclose = (e) => {
            console.log("websocket disconnected");
            //FIXME congestion control
            //retry connection
            //setTimeout(start_ws, 5000);
        }
    }
    
    start_ws();

}

main();
