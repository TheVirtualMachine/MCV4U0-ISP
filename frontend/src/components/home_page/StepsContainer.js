import React, {Component} from 'react';
import {Collapsible, CollapsibleItem} from 'react-materialize';
const {MathJax} = window;

const ICONS = {
    'Constant Times Rule': 'highlight_off',
    'Power Rule': 'filter_none',
    'Exponent Rule': 'explicit',
    'Constant Rule': 'copyright',
    'Trig Rule': 'signal_cellular_null',
    'U Rule': 'format_underlined',
    'Add Rule': 'add',
    'Don\'t Know Rule': 'help_outline',
    'Parts Rule': 'donut_large'
}

String.prototype.capitalize = function () {
    return this.replace(/(^|\s)\S/g, l => l.toUpperCase())
}

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
        let {name, text, substeps} = step;
        name = name.capitalize();
        return (
            <CollapsibleItem header={name} icon={ICONS[name]}>
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