import React, {Component} from 'react';
import {Navbar, Row, Col, Card, ProgressBar} from 'react-materialize';
import GrapherConfigPanel from './GrapherConfigPanel';
import StepsContainer from './StepsContainer';
import './HomePage.css';

const IntegralDisplay = ({fcn, integral, lower, upper, definiteIntegral}) => {
  return (
    <div>
      <span className="flow-text">Integrals:&nbsp;</span>
      <span>{`$$\\int ${fcn} dx = ${integral} + C $$`}</span>
      <span>{`$$\\int_{${lower}}^{${upper}} ${fcn} dx = ${definiteIntegral} $$`}</span>
    </div>
  );
}

const gcf = (a, b) => {
  while (b > 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

const RiemannSumDisplay = ({fcn, sum, samples, upper, lower}) => {
  let diff = upper - lower;
  let divisor = gcf(diff, samples);
  let reducedFraction;
  if (divisor === samples) {
    reducedFraction = diff / divisor;
  } else {
    reducedFraction = `\\frac{${diff / divisor}}{${samples / divisor}}`;
  }

  return (
    <div>
      <span className="flow-text">Riemann Sum:&nbsp;</span>
      <span>{`$$ \\sum_{i=1}^{${samples}} ${fcn.replace('x', 'x_i')} \\Delta x =  ${sum}, $$`}</span>
      <span>{`Where \\( \\Delta x = \\frac{${upper} - ${lower}}{${samples}} = ${reducedFraction} \\)`}</span>
    </div>
  );
}

class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      integral: '$$\\frac{x^2}{2}$$',
      loading: false,
      sum: 3520,
      steps: {
        name: '',
        text: '',
        substeps: []
      }
    }
  }

  get showStuff(){
    return this.state.function && !this.state.loading;
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
            <Card
              actions={[this.showStuff && (<IntegralDisplay fcn={this.state.function} {...this.state}/>)]}>
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
              actions={[this.showStuff && (<RiemannSumDisplay fcn={this.state.function} {...this.state}/>)]}>
              {this.state.loading
                ? <ProgressBar/>
                : <div
                  dangerouslySetInnerHTML={{
                  __html: this.state.graph
                }}></div>}
              <div
                dangerouslySetInnerHTML={{
                __html: this.state.note
              }}></div>
            </Card>
          </Col>
        </Row>
        <Row id="steps">
          <h4>Steps</h4>
          <Col s={12} m={6}>
            {this.showStuff && <StepsContainer steps={this.state.steps}/>}
          </Col>
        </Row>
      </div>
    )
  }
}
export default HomePage;