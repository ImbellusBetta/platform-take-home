/**
 * API Interface to the MAPS app on the server
 */
import client from './client';

/**
 * Get the MAPS config
 * @returns {Promise} Maps config object
 */
function config() {
	return client.get('/maps/config');
}

/**
 * Forward Geocode search
 * @param {string} address The human post address to search for
 * @returns {Promise} Object with latitude/longitude keys
 */
function search(address) {
	return client.get('/maps/geocode/search?address=' + encodeURIComponent(address))
	.then((result) => {
		return result.location;
	});
}

/**
 * Reverse Geocode search
 * @param {string|float} latitude
 * @param {string|float} longitude
 * @returns {Promise} Array of strings of all addresses at this point, highest priority to lowest
 */
function reverse(latitude, longitude) {
	return client.get('/maps/geocode/reverse?location=' + encodeURIComponent(latitude + ',' + longitude))
	.then((result) => {
		return result.addresses;
	});
}

/**
 * Approximate distance calculation between two latitude/longitude points on earth
 * @param {string|float} latitude1
 * @param {string|float} longitude1
 * @param {string|float} latitude2
 * @param {string|float} longitude2
 * @returns {float} Distance in KM between two points
 */
function distance(latitude1, longitude1, latitude2, longitude2) {
	return client.get('/maps/distance/calculate?location1=' +
		encodeURIComponent(latitude1 + ',' + longitude1) +
		'&location2=' +
		encodeURIComponent(latitude2 + ',' + longitude2))
	.then((result) => {
		return result.distance;
	});
}

export default {
	config: config,
	search: search,
	reverse: reverse,
	distance: distance
};