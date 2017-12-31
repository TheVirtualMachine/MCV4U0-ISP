import React, {Component} from 'react';
import {Navbar, Row, Col} from 'react-materialize';
import GrapherConfigPanel from './GrapherConfigPanel';
import './HomePage.css';

class HomePage extends Component {

  render() {
    return (
      <div className="HomePage">
        <Navbar brand='Riemann Sum Calculator'></Navbar>
        <Row id="calculators">
          <Col s={12} m={6}>
            <GrapherConfigPanel/>
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