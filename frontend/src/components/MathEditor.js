import React, {Component} from 'react';
const {MathQuill} = window;
const MQ = MathQuill.getInterface(2);

class MathEditor extends Component {
    componentDidMount() {
        if (this.props.editable) {
            let field = MQ.MathField(this.refs.span, {
                spaceBehavesLikeTab: true,
                autoCommands: 'pi sqrt',
                handlers: {
                    edit: function () {
                        console.log(field.latex());
                    }
                }
            });

        } else {
            MQ.StaticMath(this.refs.span);
        }
    }

    render() {
        return <span
            ref='span'
            className={[
            "math-field", this.props.className || ''
        ].join(' ')}
            style={this.props.style}>{this.props.children}</span>;
    }
}

export default MathEditor;