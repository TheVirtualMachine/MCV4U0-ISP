import React, {Component} from 'react';
const {MathJax} = window;
console.log(window);

class StepsContainer extends Component {
    componentDidUpdate() {
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    }

    renderSteps(arr) {
        if (!arr) 
            return;
        return (
            <ul>
                {arr.map(val => {
                    if (val instanceof Array) {
                        return this.renderSteps(val);
                    } else {
                        console.log(val);
                        return (
                            <li>
                                {val}
                            </li>
                        );
                    }
                })}
            </ul>
        );
    }

    render() {
        return (
            <div>
                {this.renderSteps(this.props.steps)}
            </div>
        );
    }
}

export default StepsContainer;