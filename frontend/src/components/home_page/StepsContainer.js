import React, {Component} from 'react';
import {Collapsible, CollapsibleItem, Modal, Button} from 'react-materialize';
import Steps from './derivations/derivations';

const {MathJax} = window;

const capitalize = word => word.replace(/(^|\s)\S/g, l => l.toUpperCase())

const RULES = {
    'Constant Times Rule': {
        icon: 'highlight_off',
        derivation: Steps.ConstantTimesRule
    },
    'Power Rule': {
        icon: 'filter_none',
       derivation: Steps.PowerRule
    },
    'Exponent Rule': {
        icon: 'explicit'
    },
    'Constant Rule': {
        icon: 'copyright',
        derivation: Steps.ConstantRule
    },
    'Trig Rule': {
        icon: 'signal_cellular_null'
    },
    'U Rule': {
        icon: 'format_underlined'
    },
    'Add Rule': {
        icon: 'add',
        derivation: Steps.AddRule
    },
    'Don\'t Know Rule': {
        icon: 'help_outline'
    },
    'Parts Rule': {
        icon: 'donut_large'
    },
    'Reciprocal Rule': {
        icon: 'vertical_align_center'
    },
    'Rewrite Rule': {
        icon: 'mode_edit'
    }
}

class StepsContainer extends Component {
    constructor(props) {
        super(props);
    }

    componentDidUpdate() {
        MathJax
            .Hub
            .Queue(["Typeset", MathJax.Hub]);
    }

    renderSteps(step) {
        let {name, text, substeps} = step;

        name = capitalize(name);
        let {icon, derivation} = RULES[name];

        return (
            <CollapsibleItem header={name} icon={icon}>
                <p className="rule-text">{text}</p>
                {derivation
                    ? <Modal
                            header={`Derivation of the ${name}`}
                            trigger={(
                            <Button>
                                Derivation
                            </Button>
                        )}>
                            {derivation}
                        </Modal>
                    : null}
                {substeps.map((substep, i) => {
                    return (
                        <Collapsible key={`rule-${i}`}>
                            {this.renderSteps(substep)}
                        </Collapsible>
                    );
                })}

            </CollapsibleItem>
        );
    }

    render() {
        return (
            <Collapsible>
                {this.renderSteps(this.props.steps)}
            </Collapsible>
        );
    }
}

export default StepsContainer;