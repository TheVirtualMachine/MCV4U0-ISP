import React, {Component} from 'react';
import {
    Row,
    Col,
    Input,
    Button,
    Icon,
    Collapsible,
    CollapsibleItem
} from 'react-materialize';
import MathEditor from '../MathEditor';
import {MaterialPicker} from 'react-color';
import './HomePage.css';

class GrapherConfigPanel extends Component {
    constructor(props) {
        super(props);
        this.state = {
            posColor: 'red',
            negColor: 'blue'
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
                <Row
                    id='n-slider'
                    className='range-field'
                    style={{
                    width: '95%'
                }}>
                    <label htmlFor="n-slider">Number of samples</label>
                    <Icon left>graphic_eq</Icon>
                    <input type="range" min={5} max={100} step={5} defaultValue={5}/>
                </Row>
                <Row
                    id='handed'
                    style={{
                    alignItems: 'center'
                }}>
                    <Col s={6} l={4} className='aligned'>
                        <Input type='select' label='Handedness' defaultValue={'left'} icon='pan_tool'>
                            <option value='left'>Left</option>
                            <option value='center'>Center</option>
                            <option value='right'>Right</option>
                        </Input>
                    </Col>
                    <Col
                        s={6}
                        l={4}
                        style={{
                        paddingTop: '25px'
                    }}>
                        <Input type='checkbox' label='Graph Running Area'/>
                    </Col>
                    <Col s={12} l={4}>
                        <label>Colours</label>
                        <Collapsible
                            style={{
                            'i': {
                                color: 'red'
                            }
                        }}>
                            <CollapsibleItem
                                header='Positive'
                                icon='add_circle'
                                style={{
                                color: this.state.posColor
                            }}>
                                <MaterialPicker/>
                            </CollapsibleItem>
                            <CollapsibleItem
                                header='Negative'
                                icon='remove_circle'
                                style={{
                                color: this.state.negColor
                            }}>
                                <MaterialPicker/>
                            </CollapsibleItem>
                        </Collapsible>
                    </Col>
                </Row>
                <Row id='graph-btn' className='aligned centered'>
                    <Button className='red'>Graph
                        <Icon left>show_chart</Icon>
                    </Button>
                </Row>
            </div>
        )
    }
}
export default GrapherConfigPanel;