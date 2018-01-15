import React, {Component} from 'react';
import {Navbar, Row, Col, Card} from 'react-materialize';
import GrapherConfigPanel from './GrapherConfigPanel';
import StepsContainer from './StepsContainer';
import './HomePage.css';

class HomePage extends Component {

  constructor(props) {
    super(props);
    this.state = {
      payload: {}
    }
  }

  render() {
    return (
      <div className="HomePage">
        <Navbar brand='Riemann Sum and Integral Calculator'></Navbar>
        <Row id="calculators">
          <Col s={12} m={6}>
            <Card>
              <GrapherConfigPanel
                updatePageState={this
                .setState
                .bind(this)}/>
            </Card>
          </Col>
          <Col s={12} m={6}>
            <Card>
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
    );
  }
}
export default HomePage;