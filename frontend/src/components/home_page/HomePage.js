import React, {Component} from 'react';
import {Navbar, Row, Col, Input, Icon} from 'react-materialize';
import './HomePage.css';

const {MathQuill} = window;
const MQ = MathQuill.getInterface(2);

class HomePage extends Component {

  componentDidMount() {
    for (let span of document.getElementsByClassName('static-math')) {
      MQ.StaticMath(span);
    }

    let mathFieldSpan = document.getElementById('math-field');
    var mathField = MQ.MathField(mathFieldSpan, {
      spaceBehavesLikeTab: true,
      autoCommands: 'pi sqrt',
      handlers: {
        edit: function () {
          console.log(mathField.latex());
        }
      }
    });
  }

  render() {
    return (
      <div className="HomePage">
        <Navbar brand='Riemann Sum Calculator'></Navbar>

        <Row id="calculators">
          <Col s={12} m={6}>
            <Row id='mathquill'>
              <span className="homepage__math static-math">f(x)\ =</span>
              <span className="homepage__math" id="math-field"></span>
            </Row>
            <Row id='x-range' className="centered-aligned">
              <Input
                validate
                type="text"
                defaultValue={0}
                id='lower-lim'
                label='Limits'
                icon='space_bar'/>
              <span className="homepage__math static-math">\leq\ x\ \leq</span>
              <Input validate type="text" defaultValue={20} id='upper-lim'/>
            </Row>
            <Row id='n-slider'></Row>
            <Row id='handed'>
              <Col s={12} m={6}>
                <Input type='select' label='Handedness' defaultValue={'left'} icon='pan_tool'>
                  <option value='left'>Left</option>
                  <option value='center'>Center</option>
                  <option value='right'>Right</option>
                </Input>
              </Col>
              <Col s={12} m={6}>
                <Icon>show_chart</Icon>
                <Input type='checkbox' label='Graph Running Area'/>
              </Col>
            </Row>
            <Row id='mathquill'></Row>
            <Row id='running-area'></Row>
            <Row id='graph-btn'></Row>
          </Col>
          <Col s={12} m={6}>
            B
          </Col>
        </Row>
        <Row id="steps"></Row>
      </div>
    );
  }
}

export default HomePage;