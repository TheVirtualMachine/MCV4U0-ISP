import React, {Component} from 'react';
import {
  Navbar,
  Row,
  Col,
  Card,
  Button,
  Icon
} from 'react-materialize';
import GrapherConfigPanel from './GrapherConfigPanel';
import './HomePage.css';

class HomePage extends Component {

  GraphButton() {
    return (
      <Button waves='light' className='red'>Graph
        <Icon left>show_chart</Icon>
      </Button>
    )
  }

  render() {
    return (
      <div className="HomePage">
        <Navbar brand='Riemann Sum and Integral Calculator'></Navbar>
        <Row id="calculators">
          <Col s={12} m={6}>
            <Card actions={[this.GraphButton()]}>
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