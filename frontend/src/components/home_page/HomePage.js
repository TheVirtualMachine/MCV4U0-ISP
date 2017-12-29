import React, {Component} from 'react';
import {Navbar, Row, Col} from 'react-materialize';

const {MathQuill} = window;
const MQ = MathQuill.getInterface(2);

class HomePage extends Component {

  componentDidMount() {
    let mathFieldSpan = document.getElementById('math-field');
    var mathField = MQ.MathField(mathFieldSpan, {
      spaceBehavesLikeTab: true, // an example config option, for more see:
      //   http://docs.mathquill.com/en/latest/Config/
      handlers: {
        edit: function () {
          // retrieve, in LaTeX format, the math that was typed:
          console.log(mathField.latex());
        }
      }
    });
  }

  render() {
    return (
      <div className="HomePage">
        <Navbar center brand='Riemann Sum Calculator'></Navbar>

        <Row id="calculators">
          <Col s={12} m={6}>
            <span id="math-field">y=mx+b</span>
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