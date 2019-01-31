import React from 'react';
import PropTypes from 'prop-types';
import { Map, Marker, GoogleApiWrapper } from 'google-maps-react';

/**
 * Google Maps Wrapper
 *
 * This component interfaces with Googles client side javascript APIs (lazy loaded)
 * to provide a Google Map inside a react project
 */

class MapContainer extends React.Component {
	static propTypes = {
		/**
		 * Your GoogleMaps API key
		 */
		apiKey: PropTypes.string.isRequired,
		/**
		 * The latitude of the marker
		 */
		latitude: PropTypes.string.isRequired,
		/**
		 * The longitude of the marker
		 */
		longitude: PropTypes.string.isRequired
	}

	render() {
		return (
			<Map
			style={{width:'80%', height:'50%'}}
			center={{
				lat: this.props.latitude,
				lng: this.props.longitude
			}}
			google={this.props.google}
			zoom={this.props.latitude ? 15 : 2}>

			{ this.props.latitude &&
			<Marker
				title={'Location'}
				position={{lat: this.props.latitude, lng: this.props.longitude}} />
			}
			</Map>
		);
	}
}

export default GoogleApiWrapper((props) => {
	return { apiKey: props.apiKey };
})(MapContainer);