import React, {Component} from 'react';
import {
    Row,
    Col,
    Input,
    Collapsible,
    CollapsibleItem,
    Icon
} from 'react-materialize';
import MathEditor from '../MathEditor';
import {BlockPicker} from 'react-color';
import './HomePage.css';

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

class GrapherConfigPanel extends Component {
    constructor(props) {
        super(props);
        this.state = {
            posColor: 'blue',
            negColor: 'red'
        }
    }

    handleColorChange(pos) {
        return ({hex}) => {
            if (pos) {
                this.setState({posColor: hex});
            } else {
                this.setState({negColor: hex});
            }
        };
    }

    render() {
        return (
            <div id="config-panel">
                <Row id='mathquill' className='aligned'>
                    <MathEditor
                        style={{
                        marginLeft: '10px'
                    }}>f(x)\ =</MathEditor>
                    <MathEditor editable/>
                </Row>
                <Row id='x-range' className='aligned'>
                    <Input
                        type="text"
                        defaultValue={0}
                        id='lower-lim'
                        label='Limits'
                        icon='space_bar'/>
                    <MathEditor>\leq\ x\ \leq</MathEditor>
                    <Input type="text" defaultValue={20} id='upper-lim'/>
                </Row>
                <Row id='n-slider' className='range-field'>
                    <label htmlFor="n-slider">Number of samples</label>
                    <Icon left>graphic_eq</Icon>
                    <input type="range" min={5} max={100} step={5} defaultValue={5}/>
                </Row>
                <Row id='handed'>
                    <Col s={6} l={4} className='aligned'>
                        <Input type='select' label='Handedness' defaultValue={'left'} icon='pan_tool'>
                            <option value='left'>Left</option>
                            <option value='center'>Center</option>
                            <option value='right'>Right</option>
                        </Input>
                    </Col>
                    <Col id='running-area' s={6} l={4}>
                        <Input type='checkbox' label='Graph Running Area'/>
                    </Col>
                    <Col s={12} l={4}>
                        <label>Colours</label>
                        <Collapsible>
                            <CollapsibleItem
                                header='Positive'
                                icon='add_circle'
                                style={{
                                color: this.state.posColor
                            }}>
                                <BlockPicker
                                    triangle='hide'
                                    color={this.state.posColor}
                                    colors={SWATCHES}
                                    onChangeComplete={this
                                    .handleColorChange(true)
                                    .bind(this)}/>
                            </CollapsibleItem>
                            <CollapsibleItem
                                header='Negative'
                                icon='remove_circle'
                                style={{
                                color: this.state.negColor
                            }}>
                                <BlockPicker
                                    triangle='hide'
                                    color={this.state.negColor}
                                    colors={SWATCHES}
                                    onChangeComplete={this
                                    .handleColorChange(false)
                                    .bind(this)}/>
                            </CollapsibleItem>
                        </Collapsible>
                    </Col>
                </Row>
            </div>
        )
    }
}
export default GrapherConfigPanel;