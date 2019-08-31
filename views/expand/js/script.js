

import FSM from './fsm.js'
import './jss.js'

const SHADOW = '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.1)'
//const SHADOW_UP = '0 0px 16px 3px rgba(0, 0, 0, 0.3), 0 12px 40px 3px rgba(0, 0, 0, 0.2)'
const SHADOW_UP = '0 4px 30px 4px rgba(0, 0, 0, 0.2)'

const spacing_unit = '16px'

function print(s) {console.log(s)}


function to_px(s) {

    let px = 0

    if (s.endsWith('vh'))
        px = parseFloat(s.slice(0, -2)) / 100 * window.innerHeight
    else if (s.endsWith('vw'))
        px = parseFloat(s.slice(0, -2)) / 100 * window.innerWidth
    else if (s.endsWith('px'))
        px = parseFloat(s.slice(0, -2))
    else
        px = parseFloat(s)
    return String(px) + 'px'
}

function px_to_float(s) {
    return parseFloat(s.slice(0, -2))

}

class Expand {

    constructor(exp_canvas, height='50vh', margin='15vh', num_cols=2) {

        this.on_transition = false

        this.canvas = exp_canvas

        this.height = height
        this.margin = margin
        this.num_cols = num_cols

        //HTML
        this.create_nodes()

        //CSS
        this.register_fsm()

        //JS
        this.register_listener()

        this.fsm.to_state('start', {t: this, previous_state: this.fsm.state})

    }

    create_nodes() {
    
        //Create boxes
        let boxes = []
        for (let i = 0; i < this.canvas.children.length; i ++)
            boxes.push(this.create_box(this.canvas.children[i], i))

        //Remove children
        while(this.canvas.firstChild) 
            this.canvas.removeChild(this.canvas.firstChild)

        //Add rows and boxes into DOM
        let row = undefined
        boxes.map((box, i) => {

            if (i % this.num_cols == 0) {
                row = document.createElement('div')
                this.canvas.appendChild(row)
            }
            box.box_index = i % this.num_cols
            row.appendChild(box)
        })
    
    }

    register_fsm() {

        const open_row_duration = '.5s ease'
        const open_side_duration = '.7s ease'
        const open_box_duration = '.7s cubic-bezier(1, 0, .5, 1)'

        const close_row_duration = '.7s ease'
        const close_side_duration = '.7s ease'
        const close_box_duration = '.5s ease'

        const hover_box_duration = '.3s ease'
        const unhover_box_duration = '.3s ease'

        const show_info_duration = `.2s ease`
        const hide_info_duration = `.2s ease`



        let canvas = this.canvas

        //add canvas
        this.fsm = new FSM(
        
            {element: canvas, update: (e, state, args) => {

                const margin = args.t.margin
                const num_cols = args.t.num_cols
                const height = args.t.height

                let style = `
                    position: absolute;
                    width: 100vw;
                    top: 0;
                    left: 0;
                    padding-bottom: ${margin};
                    transition: all .7s ease;
                `
                if (state.startsWith('open')) {

                    let row_rec = args.box.parentElement.getBoundingClientRect()

                    e.style.cssText = style + `
                        transform: translateY(calc(${-row_rec.top}px - ${margin}));
                        transition: all ${open_row_duration};
                    `
                }
                else if (state == 'hover') {
                    //When close a box
                    e.style.cssText = style + `transition: all ${close_row_duration};`
                }
                else if (e.style.cssText != style)
                    e.style.cssText = style
            }}
        )

 


        for (let row of canvas.children) {
            

            //add row
            this.fsm.add(
            
                {element: row, update: (e, state, args) => {

                    const margin = args.t.margin
                    const num_cols = args.t.num_cols
                    const height = args.t.height

                    let style = `
                        white-space: nowrap;
                
                        position: relative;

                        box-sizing: border-box;
                        height: calc(${height} + ${margin});
                        width: 100%;
                        top: 0;
                        left: 0;
            
                        padding-top: ${margin};

                        margin-top: 0px;
                        margin-bottom: 0px;
                        transition: all .7s ease;
                    `

                    if (state.startsWith(`open`) && args.box.parentElement == e) {

                        let row_rec = args.box.parentElement.getBoundingClientRect()

                        const num_cols = args.t.num_cols
                        const box_margin = args.t.margin
                        const box_width = `calc((100% - ${box_margin})/${num_cols} - ${box_margin})`
                        const box_height = args.t.height
                        const box_left = `calc(${box_margin} + (${box_width} + ${box_margin}) * ${args.box.box_index})`

                        e.style.cssText = style + `
                            margin-top: calc(${row_rec.top}px + ${margin}); 
                            margin-bottom: ${window.innerHeight - row_rec.bottom}px;

                            transform: translateX(calc(-1 * ${box_left}));
                            transition: 
                                margin ${open_row_duration},
                                transform  ${open_side_duration};
                        `
                    }
                    else if (state == 'hover' && args.box.parentElement == e) {
                        e.style.cssText = style + `
                            transition: 
                                transform ${close_side_duration},
                                margin ${close_row_duration};
                        `
                        
                    }
                    else if (e.style.cssText != style)
                        e.style.cssText = style
                
                }}
            )

            for (let box of row.children) {
            
                this.fsm.add(

                    //Add image div
                    {element: box.img_div, update: (e, state, args) => {
                    
                        let style = `
                            position: relative;
                            top: 0;
                            left: 0;
                            height: 100%;
                            width: 40%;

                            background-image: url(${e.img_src});
                            background-size: cover;
                            background-position: center;

                            overflow: hidden;
                            display: inline-flex;
                            align-items: center;
                            justify-content: center;
                        `
                        if (state == 'open') 
                            e.style = style + `
                                width: 60%;
                                transition: width ${open_box_duration};
                            `
                        else 
                            e.style = style + `transition: width ${close_box_duration};`
                        
                    
                    }}, 
                    //Add content div
                    {element: box.content_div, update: (e, state, args) => {

                        let style = `
                        
                            white-space: normal;
                            position: relative;
                            top: 0;
                            height: 100%;
                            width: 60%;
                            display: inline-flex;
                            flex-direction: column;
                            justify-content: center;

                            overflow: hidden;

                            box-sizing: border-box;
                            padding: 5%;
                        
                        `
                        if (state == 'open') 
                            e.style = style + `
                                width: 40%;
                                transition: width ${open_box_duration};
                            `
                        else 
                            e.style = style + `transition: width ${close_box_duration};`
                       
                    
                    
                    
                    }},

                    //add box
                    {element: box, update: (e, state, args) => {
 
                        const margin = args.t.margin
                        const num_cols = args.t.num_cols
                        const height = args.t.height
                
                        let style = `
                            /*background-color: white;*/

                            display: inline-block;
                            vertical-align: top;

                            position: relative;

                            width: calc((100% - ${margin})/${num_cols} - ${margin});
                            margin-left: ${margin};
                            height: calc(${height});

                            box-shadow: none;

                            transition: all ${hover_box_duration};
                        `
                        if (state == `open` && args.box == e) {

                            let row_rec = args.box.parentElement.getBoundingClientRect()
                                        
                            //const box_left = `calc(${box_rec.left}px)`

                            const num_cols = args.t.num_cols
                            const box_margin = args.t.margin
                            const box_width = `(calc((100vw - ${box_margin})/${num_cols} - ${box_margin}))`
                            const box_left = `calc(${box_margin} + (${box_width} + ${box_margin}) * ${args.box.box_index})`
                            const box_top = `calc(${row_rec.top}px + ${box_margin})`

                            //FIXME a bit larger than full screen 
                            const eps = '4px'
                        
                            box.style.cssText = style + `
                                margin-left: calc(${margin} + ${box_left});
                                margin-right: calc(100vw - ${box_width} - ${box_left} + ${margin});

                                transform: translate(calc(0px - ${box_left} - ${eps}), calc(0px - ${box_top} - ${eps}));
                                width: calc(100vw + ${eps} * 2);
                                height: calc(100vh + ${eps} * 2);

                                z-index: 1;
                                box-shadow: none;

                                transition: 
                                    margin ${open_side_duration}, 

                                    top ${open_box_duration},
                                    left ${open_box_duration},
                                    width ${open_box_duration},
                                    height ${open_box_duration},
                                    transform ${open_box_duration},
                                    box-shadow ${open_box_duration};
                            `
                        }

                        else if (state == `hover` && args.box == e) {

                            let row_rec = args.box.parentElement.getBoundingClientRect()

                            const num_cols = args.t.num_cols
                            const box_margin = args.t.margin
                            const box_height = args.t.height
                            const box_width = `calc((100vw - ${box_margin})/${num_cols} - ${box_margin})`
                            
                            const box_left = `calc(${box_margin} + (${box_width} + ${box_margin}) * ${args.box.box_index})`
                            const box_top = `calc(${row_rec.top}px + ${box_margin})`

                            const d = `calc(${box_width} / 10)`

                            e.style.cssText = style + `
                                width: calc(${box_width} + ${d});
                                height: calc(${box_height} + ${d});
                                transform: translate(calc(-1 * ${d}/2), calc(-1 * ${d}/2));
                                margin-right: calc(-1 * ${d});
                                box-shadow: ${SHADOW_UP};
                            ` + (
                           //Since it can from "start" to "hover" state, which is a naive hover
                           //or from "open" to "hover"

                            args.previous_state == 'start' ? `
                                transition: 
                                    all ${hover_box_duration}; 
                            `
                            : args.previous_state == 'open' ? `
                                transition:
                                    margin-left ${close_side_duration}, 
                                    margin-right ${close_side_duration},

                                    top ${close_box_duration},
                                    left ${close_box_duration},
                                    width ${close_box_duration},
                                    height ${close_box_duration},
                                    transform ${close_box_duration},
                                    box-shadow ${close_box_duration};
                            `
                            : null
                            )

                        }

                        else if (args.previous_state == 'hover') {
                            e.style.cssText = style + `transition: all ${unhover_box_duration}` 
                        }
                        else 
                            e.style.cssText = style
                    }}, 



                    //add header
                    {element: box.header, update: (e, state, args) => {

                        //TODO formalize
                        let style = `
                            
                            position: absolute;
                            top: -70px;
                            left: 0;
                            height: 64px;
                            width: 100%;
                            background-color: white;

                            transition: all .5s ease;
                        `
                        if (state == 'open' && args.box == e.parentElement.parentElement) 
                            e.style.cssText = style + `top: 0; transition: all .5s ease 1s;`
                        
                        else 
                            e.style.cssText = style
                    
                    
                    
                    }}, 


                    {element: box.article_div, update: (e, state, args) => {

                        let h = e.children[0].getBoundingClientRect().height

                        let style = `
                            position: relative;
                            width: 100%;
                            height: 0;
                        `

                        if (state == 'hover' && e.box == args.box) {

                            let intro_height = e.box.intro.getBoundingClientRect().height

                            if (args.previous_state == 'open') 
                                e.style.cssText = style + `transition: all ${close_box_duration}`

                            else
                                e.style.cssText = style + `
                                    height: calc(${intro_height}px + 2 * ${spacing_unit});
                                    transition: all ${hover_box_duration};
                                `
                        }
                        else if (state == 'open' && e.box == args.box) {
                            e.style.cssText = style + `
                                height: 80%;
                                transition: all ${open_box_duration};
                            `
                        }
                    

                        else 
                            e.style.cssText = style + `
                                transition: all ${unhover_box_duration};
                            `
                    
                    }},

                    //add intro
                    {element: box.intro, update: (e, state, args) => {

                        const box_height = args.t.height
                        
                        let style = `
                            position: relative;
                            width: 100%;
                            margin: calc(2*${spacing_unit}) 0 0 0;
                            max-height: 20vh;
                            opacity: 0;
                        `

                        if (state == 'hover' && args.box == e.box && args.previous_state != 'open') {
                            e.style.cssText = style + `
                                opacity: 1;
                                max-height: 20vh;
                                transition: all ${show_info_duration};
                            `
                        }
                        else {
                            e.style.cssText = style + `transition: all ${hide_info_duration};`
                        }
                    
                    }},

                    //add text
                    {element: box.text, update: (e, state, args) => {
                        let style = `

                            position: absolute;
                            top: 10vh;
                            left: 0;
                            opacity: 0;
                            margin: calc(2*${spacing_unit}) 0 0 0;
                            z-index: -1;
                        `
                        if (state == 'open' && e.box == args.box) 
                            e.style.cssText = style + `top: 0; opacity: 1; z-index: 1;transition: all .3s ease .9s;`
                        
                        else 
                            e.style.cssText = style + `transition: all .3s ease;`
                    
                    
                    }}
            
                )

            
            
            }
            
            
        }
    }

    //Control the change of state of FSM
    register_listener() {

        for (let row of this.canvas.children) {

            for (let box of row.children) {
    
                box.addEventListener('click', e => {

                    if (this.on_transition || this.fsm.state == 'open') return

                    this.on_transition = true
                    this.fsm.to_state(this.fsm.state == 'open' ? 'hover'
                                    : this.fsm.state == 'hover'? 'open'
                                    : 'start', {box: box, t: this, previous_state: this.fsm.state})

                    //FIXME Modify delay to be the transition duration when opening and closing a box
                    //i.e. max(open_box_duration, close_box_duration)
                    setTimeout(() => {
                        this.on_transition = false
                    }, 1000)

                })

                box.return_btn.onclick = e => {
                    this.on_transition = true
                    this.fsm.to_state('hover', {box: box, t: this, previous_state: this.fsm.state})
                    setTimeout(() => {
                        this.on_transition = false
                    }, 1000)
                }

                box.addEventListener('mouseenter', e => {

                    //Lift effect
                    if(this.fsm.state != 'open' && !this.on_transition)
                        this.fsm.to_state('hover', {box: box, t: this, previous_state: this.fsm.state})
                })
                box.addEventListener('mouseleave', e => {

                    if (this.fsm.state != 'open' && !this.on_transition)
                        this.fsm.to_state('start', {t: this, previous_state: this.fsm.state})
                })
            }
        }
    }


    //process html attributes and convert to html elements
    create_box(item, box_index) {
        
        let box = document.createElement('div')

        let img_div = document.createElement('div')
        img_div.img_src = item.getAttribute('src')

        //Header
        let img_header = document.createElement('header')
        img_header.classList.add('mdc-elevation--z2')
        img_header.innerHTML = `

          <div class="mdc-top-app-bar__row">

            <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start">
              <button class="mdc-icon-button material-icons mdc-top-app-bar__navigation-icon--unbounded">menu</button>
              <span class="mdc-top-app-bar__title">San Francisco, CA</span> 
            </section>

            <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end">
              <button class="mdc-icon-button material-icons mdc-top-app-bar__action-item--unbounded" aria-label="Bookmark this page">arrow_back</button>
            </section>

          </div>
        `


        //Image 
        let img = document.createElement('img')
        img.style.cssText = `height: 100%;`

        //Content
        let content_div = document.createElement('div')

        let subtitle = document.createElement('div')
        subtitle.style.cssText = `
            width: 100%;
            opacity: .3;
        `
        subtitle.innerHTML = item.getAttribute('subtitle')

        let title = document.createElement('h2')
        title.style = `
            width: 100%;
            vertical-align: middle;
            margin: ${spacing_unit} 0 0 0;
        `
        title.innerHTML = item.getAttribute('title')


        let divider = document.createElement('div')
        divider.classList.add('mdc-divider')
        divider.style = `
            opacity: .4;
            height: 4px;
            width: 5em;
            align-self: start;
            margin: ${spacing_unit} 0 0 0;
        `

        let article_div = document.createElement('div')

            let intro = document.createElement('div')
            intro.innerHTML = `
                <p>${item.getAttribute('intro')}</p>
                    <button class="mdc-button">
                        <span class="mdc-button__label">Read More</span>
                        <i class="material-icons mdc-button__icon" aria-hidden="true">keyboard_arrow_right</i>
                    </button>
            
            `

            let text = document.createElement('p')
            text.innerHTML = item.getAttribute('text')


        img_div.appendChild(img)
        img_div.appendChild(img_header)

        content_div.appendChild(subtitle)
        content_div.appendChild(title)
        content_div.appendChild(divider)
        content_div.appendChild(article_div)//i.e. below the title

        //These two are toggled when open a box
        article_div.appendChild(intro)
        article_div.appendChild(text)


       
        box.appendChild(img_div)
        box.appendChild(content_div)

        box.img_div = img_div
        box.content_div = content_div

        box.header = img_header
        box.intro = intro
        box.text = text
        box.article_div  = article_div
        box.return_btn = img_header.children[0].children[1].children[0]

        intro.box = box
        text.box = box
        article_div.box = box

        return box
    
    }

}

//Usage
document.addEventListener("DOMContentLoaded", function() { 

    let exp = new Expand(document.getElementById('expcanvas'))

})

