import React, {Component} from 'react';
import {Collapsible, CollapsibleItem} from 'react-materialize';
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

    renderSteps(step) {
        console.log('step:',step)
        let {name, text, substeps} = step;
        return (
            <CollapsibleItem header={name}>
                <p className="rule-text">{text}</p>
                {substeps.map(substep => {
                    return (
                        <Collapsible>
                            {this.renderSteps(substep)}
                        </Collapsible>
                    );
                })}
            </CollapsibleItem>
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
        return (
            <Collapsible>
                {this.state.steps}
            </Collapsible>
        );
    }
}

export default StepsContainer;