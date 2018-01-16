import React, {Component} from 'react';
import {Navbar, Row, Col, Card} from 'react-materialize';
import GrapherConfigPanel from './GrapherConfigPanel';
import StepsContainer from './StepsContainer';
import './HomePage.css';

const IntegralDisplay = ({integral}) => {
  return (
    <div>
      <span className="flow-text">Indefinite Integral:&nbsp;</span>
      <span>{`\\(\\int f(x) dx = ${integral.slice(2, -2)} + C \\)`}</span>
    </div>
  );
}

const RiemannSumDisplay = ({sum}) => {
  return (
    <div>
      <span className="flow-text">Riemann Sum:&nbsp;</span>
      <span>{`\\( \\sum f(x) \\Delta x = ${sum.slice(2,-2)} \\)`}</span>
    </div>
  );
}

class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      integral: '$$\\frac{x^2}{2}$$',
      sum: '\\(3520.0\\)'
    }
  }

  componentWillUpdate() {
    window
      .MathJax
      .Hub
      .Queue(["Typeset", window.MathJax.Hub]);
  }

  render() {
    return (
      <div className="HomePage">
        <Navbar brand='Riemann Sum and Integral Calculator'></Navbar >
        <Row id="calculators">
          <Col s={12} m={6}>
            <Card actions={[(<IntegralDisplay integral={this.state.integral}/>)]}>
              <GrapherConfigPanel
                updatePageState={this
                .setState
                .bind(this)}/>
            </Card>
          </Col>
          <Col s={12} m={6}>
            <Card
              style={{
              minWidth: '100%'
            }}
              actions={[(<RiemannSumDisplay sum={this.state.sum}/>)]}>
              <div
                dangerouslySetInnerHTML={{
                __html: this.state.graph
              }}></div>
              <div
                dangerouslySetInnerHTML={{
                __html: this.state.note
              }}></div>
            </Card>
          </Col>
        </Row>
        <Row id="steps">
          <StepsContainer steps={this.state.steps}/>
        </Row>
      </div>
    )
  }
}
export default HomePage;