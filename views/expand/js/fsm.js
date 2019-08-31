
class Element {
    constructor(target, update) {
        this.target = target
        this.update = update
    }
    //update should be overwritten
    update(e, state, ...inputs) {
        console.log('TODO: update function')
    }
}


/*
class FSM {

    constructor(...items) {

        this.elements = []
        this.edge_to_tasks = {}
        this.state = undefined

        this.add(...items)

    }
   
    to_state(state) {

        let key = `${this.state}__MAGIC__${state}`

        if (this.edge_to_tasks[key])
            for (let [element, update] of this.edge_to_tasks[key]) 
                update(element)

        this.state = state
    }

    add(...items) {

        for (let item of items) {
            if (!item) continue

            let ele = item.element

            if (ele in this.elements) 
                console.log('Warning: ')

            for (let edge of item.edges) {
                const key = `${edge.from}__MAGIC__${edge.to}`

                if (!this.edge_to_tasks[key]) 
                    this.edge_to_tasks[key] = []
                this.edge_to_tasks[key].push([ele, edge.update])

            }
        }
    }
   
}
//Usage
let divs = []

for (let i = 0; i < 10; i ++)
    divs.push(document.createElement('div'))

let fsm = new FSM(
                    {element: divs[0], edges: [
                        {from: 'start', to: 'end', update: (e) => {
                            console.log(`0: from start to end`)
                        }},
                        {from: 'end', to: 'start', update: (e) => {
                            console.log(`0: from end to start`)
                        }},
                    ]},

)

fsm.to_state('start')
fsm.to_state('end')
fsm.to_state('start')
*/


class FSM {

    constructor(...items) {
        console.log(items)

        this.elements = []
        this.add(...items)
        this.previous_state = undefined
        this.state = undefined
        
    }

    to_state(state, ...inputs) {

        let outputs = []
        for (let e of this.elements) {
            let output = e.update(e.target, state, ...inputs)
            outputs.push(output)
        }

        this.previous_state = state
        this.state = state

        return outputs
    }

    add(...items) {
        for (let t of items) {
            let e = new Element(t.element, t.update)
            this.elements.push(e)
        }
    }
}


export default FSM

