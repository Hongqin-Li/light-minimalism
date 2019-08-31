
function is_props(obj) {
    return typeof obj == 'object' && typeof obj.appendChild == 'undefined'
}

function is_html_element(obj) {
    return typeof obj.appendChild == 'function'
}

function create_element(e, ...props_or_children) {

    for (let pc of props_or_children) {

        if (!pc) 
            break

        else if (typeof pc == 'string') 
            e.appendChild(document.createTextNode(pc))

        else if (is_html_element(pc))
            e.appendChild(pc)

        else if (is_props(pc))
            for (let [prop, value] of Object.entries(pc)) {

                if (e.hasAttribute(prop))
                    console.log(`Warning: property ${prop} is overwritten.`)
                e.setAttribute(prop, value)
            }
        else 
            console.log('Error: illegal, should be string or html element or props object')
    }

    return e
}



const html_elements = ['div', 'span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'code', 'a', 'img']

//Create elements
for (let e of html_elements) 
    window[e] = (...args) => create_element(document.createElement(e), ...args)


/*
//Usage
let root = div({class: 'container'}, 'hhh', div())
document.body.appendChild(root)
console.log(root)
*/

