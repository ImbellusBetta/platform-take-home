import React from 'react';
import { Container, Row, Col, Button, Form, Card, CardHeader, CardBody } from 'reactstrap';
import Location from 'components/Location';
import Status from 'components/Status';
import services from 'services';

/**
 * Distance
 *
 * Input two latitude and longitude coordinates which
 * will be sent to the server for distance calculation
 */
class Distance extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			address: '',
			result: null,
			error: null
		};
	}

	onSubmit = () => {
		this.setState({ status: 'loading' });
		return services.maps.distance(this.state.latitude1, this.state.longitude1, this.state.latitude2, this.state.longitude2)
		.then((distance) => {
			this.setState({ message: distance.toFixed(2) + 'KM', status: 'loaded' });
		})
		.catch((err) => {
			this.setState({ message: err.messaege, status: 'error' });
		});
	}

	render() {
		return (
		<Container>
			<Row>
				<Col xs="12" md="6">
					<Card className="mt-2">
						<CardHeader>Distance between to two points</CardHeader>
						<CardBody>
							<Form>
								<Location label="Location 1" className="location1" onChange={(e, name) => { console.log(e.target.value, name); this.setState({ [name + '1']: e.target.value }); }} />
								<Location label="Location 2" className="location2" onChange={(e, name) => { console.log(e.target.value, name); this.setState({ [name + '2']: e.target.value }); }}/>
							</Form>
							<Row>
								<Col xs="3">
									<Button className="submit" onClick={this.onSubmit}>Submit</Button>
								</Col>

								<Col>
									<Status status={this.state.status} message={this.state.message}/>
								</Col>
							</Row>
						</CardBody>
					</Card>
				</Col>
				<Col>
				</Col>
			</Row>

		</Container>
		);
	}
}

export default Distance;
