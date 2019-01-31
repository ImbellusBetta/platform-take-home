import React from 'react';
import PropTypes from 'prop-types';
import { Container, Row, Col, Card, CardBody, CardHeader, Form, FormGroup, Input, Button } from 'reactstrap';
import services from 'services';
import Location from 'components/Location';
import Status from 'components/Status';
import Map from 'components/Map';

/**
 * Geocode
 *
 * This container displays two methods of inputing Geocode coordinates and a Google Map
 * of the Geocode location below it.
 *
 * Inputs:
 * 1. A human readable string where a postal address can be input
 *
 * 2. A Lat/Long box that allows degrees to be put in directly.
 */
class Geocode extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			apiKey: '',
			address: '',
			latitude: null,
			longitude: null,
			mapLatitude: 0,
			mapLongitude: 0
		};
	}

	componentDidMount() {
		// Load the maps api key from the server
		services.maps.config()
		.then((config) => {
			this.setState({ apiKey: config.apiKey });
		})
		.catch(() => {
			alert('Failed to load config - is the server running?');
		});
	}

	onSearch = () => {
		// Forward Geocode search
		return services.maps.search(this.state.address)
		.then((location) => {

			// Update the map with coordinates
			this.setState({
				mapLatitude: location.latitude,
				mapLongitude: location.longitude
			});

			// Return string for display
			return location.latitude + ',' + location.longitude;
		});
	}

	onReverse = () => {
		// Reverse Geocode search

		// First update the map with our coords
		this.setState({
			mapLatitude: this.state.latitude,
			mapLongitude: this.state.longitude
		});

		// Then resolve those back to a street address
		return services.maps.reverse(this.state.latitude, this.state.longitude)
		.then((addresses) => {
			// Only show the first address on the UI
			return addresses[0];
		});
	}

	onAddressChange = (e) => {
		// Update the address as users type
		this.setState({ address: e.target.value });
	}

	onLocationChange = (e, name) => {
		// Update the lat/long as users type
		this.setState({ [name]: e.target.value });
	}

	render() {
		return (
		<Container>
			<Row>
				<Col xs="12" md="6">
					<InputCard className="addressCard" onSubmit={this.onSearch} title="Geocode Search">
						<FormGroup>
							<Input type="text" className="address" placeholder="1 Someplace, Some State" onChange={this.onAddressChange}/>
						</FormGroup>
					</InputCard>
				</Col>
				<Col>
					<InputCard className="locationCard" onSubmit={this.onReverse} title="Geocode Reverse">
						<FormGroup>
							<Location onChange={this.onLocationChange}/>
						</FormGroup>
					</InputCard>
				</Col>
			</Row>
			{ this.state.apiKey && // Only attempt to render if we have an API key, app still works without it
			<Map latitude={this.state.mapLatitude} longitude={this.state.mapLongitude} apiKey={this.state.apiKey}/>
			}
		</Container>
		);
	}
}

/**
 * InputCard
 *
 * InputCard is a single input card on the Geocode screen. It handles
 * updating visual state for API calls, but doesn't understand the state
 * it holds in anyway.
 */
class InputCard extends React.Component {
	static propTypes = {
		/**
		 * The title to show on the Card
		 */
		title: PropTypes.string.isRequired,
		/**
		 * Extra class names for the Element
		 */
		className: PropTypes.string
	}

	constructor(props) {
		super(props);
		this.state = {
			status: '',
			message: ''
		};
	}

	onSubmit = () => {
		this.setState({ status: 'loading' });
		this.props.onSubmit()
		.then((result) => {
			this.setState({ message: result, status: 'loaded' });
		})
		.catch((err) => {
			this.setState({ message: err.message, status: 'error' });
		});
	}

	render() {
		return (
			<Card className={'mt-2 ' + (this.props.className || '')}>
				<CardHeader>{ this.props.title }</CardHeader>
				<CardBody>
					<Form>
						{this.props.children}
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
		);
	}
}

export default Geocode;
