import React, {Component} from 'react';
import {
    Row,
    Col,
    Input,
    Collapsible,
    CollapsibleItem,
    Icon,
    Button
} from 'react-materialize';
import MathEditor from '../MathEditor';
import {BlockPicker} from 'react-color';
import 'whatwg-fetch';

import './HomePage.css';

const BASE_URL = 'https://glacial-escarpment-19739.herokuapp.com'

const SWATCHES = [
    '#D9E3F0',
    '#F47373',
    '#697689',
    '#37D67A',
    '#2CCCE4',
    '#555555',
    '#dce775',
    '#ff8a65',
    '#ba68c8',
    '#beeeef'
]

const ColorPickerItem = (props) => {
    return (
        <CollapsibleItem
            header={props.header}
            icon={props.icon}
            style={{
            color: props.color
        }}>
            <BlockPicker
                triangle='hide'
                color={props.color}
                colors={SWATCHES}
                onChangeComplete={props.onChangeComplete}/>
        </CollapsibleItem>
    );
};

class GrapherConfigPanel extends Component {
    constructor(props) {
        super(props);
        this.state = {
            equation: 'x^2',
            lower: 0,
            upper: 10,
            samples: 5,
            handed: 'left',
            graphArea: false,
            posColor: '#0000ff',
            negColor: '#ff0000',
            valid: {
                // NOTE: those that are excluded have a closed set of results or already reject
                // invalid results.
                equation: true,
                lower: true,
                upper: true
            }
        }
    }

    componentDidMount() {
        this.submit();
        this.updateGraph();
    }

    handleEquationChange(latex) {
        //TODO: validate
        this.setState({equation: latex});
    }

    handleLimitChange(upper) {
        //TODO: this is the ugliest function I've ever written and I'm sorry.
        return ({
            target
        }, val) => {
            let valid = !isNaN(val);
            if (upper) {
                valid = valid && val > this.state.lower;
            } else {
                valid = valid && this.state.upper > val;
            }
            if (upper) {
                this.setState((prevState) => {
                    return {
                        valid: {
                            ...prevState.valid,
                            upper: valid
                        }
                    };
                });
            } else {
                this.setState((prevState) => {
                    return {
                        valid: {
                            ...prevState.valid,
                            lower: valid
                        }
                    };
                });
            }
            if (!valid) {
                //reject
                return;
            }
            this.setState(upper
                ? {
                    upper: parseFloat(val, 10)
                }
                : {
                    lower: parseFloat(val, 10)
                });
        };
    }

    handleSampleChange({target}) {
        this.setState({
            samples: target.value
        }, () => this.updateGraph());
    }

    handleHandedChange(event, val) {
        this.setState({
            handed: val
        }, () => this.updateGraph());
    }

    handleGraphAreaChange(event, val) {
        this.setState({
            graphArea: val
        }, () => this.updateGraph());
    }

    handleColorChange(pos) {
        return ({hex}) => {
            this.setState(pos
                ? {
                    posColor: hex
                }
                : {
                    negColor: hex
                });
        };
    }

    updateGraph() {
        let {
            equation,
            lower,
            upper,
            samples,
            handed,
            graphArea,
            posColor,
            negColor
        } = this.state;
        const request = `${BASE_URL}/graph?f=${encodeURIComponent(equation)}&lower=${lower}&upper=${upper}&n=${samples}&handed=${handed}&sum=${graphArea}&pos=${encodeURIComponent(posColor)}&neg=${encodeURIComponent(negColor)}`;
        fetch(request, {mode: 'cors'})
            .then(result => result.json())
            .then(result => this.props.updatePageState({
                ...result,
                lower: this.state.lower,
                upper: this.state.upper,
                samples: this.state.samples
            }))
            .catch(error => {
                console.log(error);
                this
                    .props
                    .updatePageState({

                        loading: false,
                        graph: '<div><h1>Graphing Failed</h1><h3>Something went wrong. Sorry about that.</h3></d' +
                                'iv>'
                    });
            });
    }

    submit() {
        const invalid_fields = Object
            .entries(this.state.valid)
            .filter(([key, val]) => !val);
        const invalid_field_names = invalid_fields.map(([key, val]) => key);

        if (invalid_fields.length > 0) {
            //TODO: reject
            alert('The following fields are invalid:\n', invalid_field_names.join(' '))
        } else {

            this
                .props
                .updatePageState({loading: true})

            //TODO: graph/allow graph
            let {equation, lower, upper} = this.state;
            const request = `${BASE_URL}/integrate?f=${encodeURIComponent(equation)}&lower=${lower}&upper=${upper}`;

            fetch(request, {mode: 'cors'})
                .then(result => result.json())
                .then(result => this.props.updatePageState({
                    ...result,
                    loading: false
                }))
                .catch(error => {
                    console.log(error);
                    this
                        .props
                        .updatePageState({loading: false});
                }); //TODO: errortrap
            this.updateGraph();
        }
    }

    render() {
        return (
            <div id="config-panel">
                <Row id='mathquill' className='aligned'>
                    <MathEditor
                        style={{
                        marginLeft: '10px'
                    }}>f(x)\ =</MathEditor>
                    <MathEditor
                        editable
                        onChange={this
                        .handleEquationChange
                        .bind(this)}/>
                </Row>
                <Row id='x-range' className='aligned'>
                    <Input
                        onChange={this
                        .handleLimitChange(false)
                        .bind(this)}
                        type="text"
                        defaultValue={0}
                        id='lower-lim'
                        label='Limits'
                        icon='space_bar'
                        validate={this.state.valid.lower}
                        className={(!this.state.valid.lower && 'invalid') || ''}/>
                    <MathEditor>\leq\ x\ \leq</MathEditor>
                    <Input
                        onChange={this
                        .handleLimitChange(true)
                        .bind(this)}
                        type="text"
                        defaultValue={10}
                        id='upper-lim'
                        validate={this.state.valid.upper}
                        className={(!this.state.valid.upper && 'invalid') || ''}/>
                </Row>
                <Row id='n-slider' className='range-field'>
                    <label htmlFor="n-slider">Number of samples</label>
                    <Icon left>graphic_eq</Icon>
                    <input
                        onChange={this
                        .handleSampleChange
                        .bind(this)}
                        type="range"
                        min={5}
                        max={100}
                        step={5}
                        defaultValue={5}/>
                </Row>
                <Row id='handed'>
                    <Col s={6} l={4} className='aligned'>
                        <Input
                            onChange={this
                            .handleHandedChange
                            .bind(this)}
                            label='Handedness'
                            defaultValue={'left'}
                            icon='pan_tool'
                            type='select'>
                            <option value='left'>Left</option>
                            <option value='center'>Center</option>
                            <option value='right'>Right</option>
                        </Input>
                    </Col>
                    <Col id='running-area' s={6} l={4}>
                        <Input
                            onChange={this
                            .handleGraphAreaChange
                            .bind(this)}
                            type='checkbox'
                            label='Graph Running Area'/>
                    </Col>
                    <Col s={12} l={4}>
                        <Collapsible>
                            <ColorPickerItem
                                header='Positive'
                                icon='add_circle'
                                color={this.state.posColor}
                                onChangeComplete={this
                                .handleColorChange(true)
                                .bind(this)}/>
                            <ColorPickerItem
                                header='Negative'
                                icon='remove_circle'
                                color={this.state.negColor}
                                onChangeComplete={this
                                .handleColorChange(false)
                                .bind(this)}/>
                        </Collapsible>
                    </Col>
                </Row>
                <Row id='submit-btn'>
                    <Button
                        onClick={this
                        .submit
                        .bind(this)}
                        className='red'
                        waves='light'>Graph
                        <Icon left>show_chart</Icon>
                    </Button>
                </Row>
            </div>
        )
    }
}
export default GrapherConfigPanel;