import React from 'react';
import PropTypes from 'prop-types';
import { Row, Col, Input, InputGroup, InputGroupAddon, Label, FormGroup } from 'reactstrap';

/**
 * Location
 *
 * Provides two styled input fields for latitude
 * and longitude text entry
 *
 */
class Location extends React.Component {

	static propTypes = {
		/**
		 * Method to call when either lat/long change
		 *
		 * @param {Event} event The browser event
		 * @param {String} name The name of the field thats changing
		 */
		onChange: PropTypes.func.isRequired,
	}

	render() {
		return (
		<FormGroup className={this.props.className}>
			<Label>{this.props.label}</Label>
			<Row>
				<Col>
					<Coordinate className="latitude" name="latitude" label="Latitude" onChange={this.props.onChange}/>
				</Col>
				<Col>
					<Coordinate className="longitude" name="longitude" label="Longitude" onChange={this.props.onChange}/>
				</Col>
			</Row>
		</FormGroup>
		);
	}
}

/*
 * Coordinate
 *
 * Helper class for a single Lat/Long Coordinate
 */
class Coordinate extends React.Component {

	onChange = (e) => {
		this.props.onChange(e, this.props.name);
	}

	render() {
		return (
			<InputGroup>
				<InputGroupAddon addonType="prepend">{ this.props.label }</InputGroupAddon>
				<Input className={this.props.className} placeholder="" onChange={this.onChange}/>
			</InputGroup>
		);
	}
}

export default Location;