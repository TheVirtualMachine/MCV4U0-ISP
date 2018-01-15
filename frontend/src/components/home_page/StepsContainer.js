import React, {Component} from 'react';
const {MathJax} = window;

class StepsContainer extends Component {
    componentDidUpdate() {
        MathJax
            .Hub
            .Queue(["Typeset", MathJax.Hub]);
    }

    renderSteps(arr) {
        if (!arr || arr.length === 0) 
            return;
        console.log('arr', arr);
        let [[name, text], ...substeps] = arr;
        console.log(name, text, substeps);

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
            <div>
                {this.renderSteps(this.props.steps)}
            </div>
        );
    }
}

export default StepsContainer;