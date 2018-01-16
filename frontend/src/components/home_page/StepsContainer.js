import React, {Component} from 'react';
const {MathJax} = window;

class StepsContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            steps: []
        };
    }

    componentWillReceiveProps({steps}) {
        this.setState({
            steps: this.renderSteps(steps)
        });
    }

    componentDidUpdate() {
        MathJax
            .Hub
            .Queue(["Typeset", MathJax.Hub]);
    }

    renderSteps(arr) {
        if (!arr || arr.length === 0) 
            return;
        
        let [rule,
            ...substeps] = arr;
        while (rule[0]instanceof Array) {
            rule = rule[0];
        }
        let [name,
            text] = rule;

        console.log('name', name, 'text', text, 'substeps', substeps.length);

        if (substeps.length > 1) {
            console.log(substeps.map(x => x[0]))
        }

        return (
            <div className="step">
                <h1>{name}</h1>
                <p className="rule-text">{text}</p>
                {substeps.map(this.renderSteps.bind(this))}
            </div>
        );

        /*return (
            <ul>
                {arr.map(val => {
                    if (val instanceof Array && val.length) {
                        return this.renderSteps(val);
                    } else {
                        return (
                            <li>
                                {val}
                            </li>
                        );
                    }
                })}
            </ul>
        );*/
    }

    render() {
        console.log('steps:', JSON.stringify(this.props.steps || []));
        return (
            <div>
                {this.state.steps}
            </div>
        );
    }
}

export default StepsContainer;