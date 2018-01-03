import React, {Component} from 'react';
import {Navbar, Row, Col, Card} from 'react-materialize';
import GrapherConfigPanel from './GrapherConfigPanel';
import './HomePage.css';

class HomePage extends Component {

  render() {
    return (
      <div className="HomePage">
        <Navbar brand='Riemann Sum and Integral Calculator'></Navbar>
        <Row id="calculators">
          <Col s={12} m={6}>
            <Card>
              <GrapherConfigPanel/>
            </Card>
          </Col>
          <Col s={12} m={6}>
            <Card>
              B
            </Card>
          </Col>
        </Row>
        <Row id="steps"></Row>
      </div>
    );
  }
}
export default HomePage;