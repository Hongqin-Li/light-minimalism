
let LM = (function() {

    // FIXME: Fix Safari
    document.addEventListener('click', event => {
        if (event.target.matches('button')) event.target.focus();
    });
    console.log("LM");

    /* Swap function
     * b = swap(a, a=b);
     */
    function swap(a) {
        return a;
    }

    /* Min-max heap implementation
     * O(1) retrival
     * O(logn) insertion and deletion
     */
    class MinMaxHeapNode {
        constructor(key, obj) {
            this.key = key;
            this.obj = obj;
            this.father = false;
            this.left = false;
            this.right = false;
            this.level = 0;
        }
        less(obj) {
            return this.key < obj.key;
        }
        swap(obj) {
            let k = this.key, o = this.obj, fa = this.father, left = this.left, right = this.right, level = this.level;
            this.key = obj.key;
            this.obj = obj.obj;
            this.father = obj.father;
            this.left = obj.left;
            this.right = obj.right;
            this.level = obj.level;
            obj.key = k;
            obj.obj = o;
            obj.father = fa;
            obj.left = left;
            obj.right = right;
            obj.level = level;
        }
    }
    class MinMaxHeap {
        constructor() {

        }
        pushup() {
        }
        pushupx(i, min) {
            while (i.father) {
                let gf = i.father.father;
                if (gf && ((min && i.key < gf.key) || (!min && i.key > gf.key)) ) {
                    i.swap(gf);
                    this.pushupx(i, min);
                }
                else 
                    break;
            }
        }
    }

    // Daemon-based congestion events handler
    // Like the thread pool
    class Worker {

        constructor() {

            this.daemon = false;
            this.jobs = [];

        }
        _start_daemon() {

            if (!this.daemon && this.jobs.length > 0) {

                this.daemon = true;
                const _this = this;
                let sleep = 0;

                (function query() {

                    if (_this.jobs.length > 0) {

                        _this.daemon = true;

                        let f = _this.jobs[0][0];
                        const min_sleep = _this.jobs[0][1];
                        const max_sleep = _this.jobs[0][2];
                        sleep = max_sleep - min_sleep;
                        f();

                        _this.jobs.shift();

                        setTimeout(query, min_sleep);
                    }
                    else {
                        if (sleep <= 0) {
                            _this.daemon = false;
                        }
                        else {
                            //FIXME tune this for performance reason
                            const dt = 200;
                            sleep -= dt;
                            setTimeout(query, dt);
                        }
                    }
                })();
            }
        }
        // Sleep after f finished
        //
        // min_sleep: the time to sleep when there are still other jobs to do
        // max_sleep: the max time to sleep when there are no other jobs 
        //
        // When a new job is added and current jobs has sleep for t in [min_sleep, max_sleep),
        // then it will finish current job at once(may be a minor delay (<=dt)) and execute the new job
        add_job(f, min_sleep=0, max_sleep=0) {
            this.jobs.push([f, min_sleep, max_sleep]);
            this._start_daemon();
        }
    }


    class LM {
        constructor() {
            this.toast_list = [];
            this.toast_daemon = 0;
        }

        _start_toast() {

            if (!this.toast_daemon && this.toast_list.length > 0) {

                this.toast_daemon = 1;

                const dt = 1000;//equal to transition-delay
                const life = 5;

                let td = document.getElementsByClassName("toast--hide")[0];
                if (!td) {
                    //toast div not provided
                    td = document.createElement("div");
                    td.className = "toast--hide";
                    td.appendChild(document.createElement("div"));
                    document.querySelector("body").appendChild(td);
                }
                const tdd = td.children[0];
                const tl = this.toast_list;

                let state = "hide";
                let _this = this;
                let l = life;

                const toast_hide_style = "toast--hide";
                const toast_show_style = "toast--show";

                setTimeout(function query() {

                    if (state == "show") {
                        if (tl.length != 0 || l <= 0) {
                            state = "hide";
                            l = life;
                            td.className = toast_hide_style;
                        }
                        else {
                            l -= 1;
                        }
                        setTimeout(query, dt);
                    }
                    else if (state == "hide") {
                        if (tl.length != 0) {

                            tdd.innerHTML = _this.toast_list[0];
                            td.className = toast_show_style;
                            tl.shift();

                            state = "show";
                            l = life;
                            setTimeout(query, dt);
                        }
                        else {
                            _this.toast_daemon = 0;
                        }
                    }
                //FIXME
                }, 10);
            }
        }

        // Fetch file specified by url and return its content string.
        fetch(url, callback) {

            fetch(url).then((response) => {
                // When the page is loaded convert it to text
                return response.text();
            })
            .then((html) => {
                callback(html);
            })
            .catch((err) => {  
                console.log('Failed to fetch page: ', err);  
            });
        }

        //usage: LM.toast("hello");
        toast(s) {
            // only the first toast is valid
            this.toast_list.push(s);
            this._start_toast();
        }

        //number of reserved top items, which are always top
        collapse_list_init(list_container, reserve_top=0) {
            list_container.worker = new Worker();
            list_container.reserve_top = reserve_top;
        }
        collapse_list_set_fixed_top(list_item, order) {
            //TODO
        }
        collapse_list_set_top(list_item, duration=500) {

            let list_container = list_item.parentElement;

            if (!list_container.worker) 
                this.collapse_list_init(list_container);

            const rt = list_container.reserve_top;

            //collapse
            list_container.worker.add_job(() => {
                list_item.classList.add("list-item--collapse");
                list_item.classList.remove("list-item--expand");
                //list_item.classList.toggle("list-item--collapse");
            }, duration, duration);

            //set top
            list_container.worker.add_job(() => {
                list_container.insertBefore(list_item, list_container.children[rt]);
                //list_item.classList.toggle("list-item--collapse");
                //list_item.classList.add("list-item--expand");
                //list_item.classList.remove("list-item--collapse");
            }, duration, duration);

            list_container.worker.add_job(() => {
                //list_item.classList.toggle("list-item--collapse");
                list_item.classList.add("list-item--expand");
                list_item.classList.remove("list-item--collapse");
            }, duration, duration);


        }

        select_handler(e) {
            e.preventDefault();
            //e.target.parentElement.previousSibling.innerHTML
        }

        modify_init(item) {
            item.worker = new Worker();
        }
        modify(item, content) {
            if (!item.worker)
                this.modify_init(item);
            // Hide
            item.worker.add_job(() => {
                item.classList.add("modify--hide");
                item.classList.remove("modify--show");
            }, 200, 200);
            // Replace and Show
            item.worker.add_job(() => {
                item.innerHTML = content;
                item.classList.add("modify--show");
                item.classList.remove("modify--hide");
            }, 500, 500);
        }

        inview(el) {
            let rect = el.getBoundingClientRect();
            return rect.bottom > 0 && rect.top < window.innerHeight;
        }
        reveal(ele) {
        
        }
    }
    return new LM();
})();
