import config from './config';

/**
 * Client
 *
 * Thin wrapper around XMLHttpRequest to provide
 * a clean simple interface for doing JSON API calls
 */

class Client {

	constructor() {
		this.baseUrl = config.baseUrl;
	}

	/**
	 * Low level HTTP request
	 * @param {object} options
	 * @returns {promise}
	 */
	request(options) {

		return new Promise((resolve, reject) => {

			let url = this.buildUrl(options.url);

			let xhr = new XMLHttpRequest();
			xhr.open(options.method || 'GET', url);
			xhr.setRequestHeader('accept', 'application/json');

			let body = options.body;
			if (options.data) {
				body = JSON.stringify(options.data);
				xhr.setRequestHeader('content-type', 'application/json');
			}
			xhr.addEventListener('load', function () {

				if (xhr.status >= 400) {
					if (xhr.responseText[0] === '{') {
						let response = JSON.parse(xhr.responseText);
						let error = new Error(response.message);
						error.error = response.error;
						reject(error);
					} else {
						reject(xhr.responseText);
					}
				}

				try {
					let contentType = this.getResponseHeader('content-type');
					if (contentType && contentType.indexOf('application/json') === 0) {
						resolve(JSON.parse(xhr.responseText));
					} else {
						resolve(xhr.responseText);
					}
				} catch (err) {
					reject(err);
				}
			}, false);
			xhr.addEventListener('error', reject, false);
			xhr.addEventListener('abort', reject, false);
			xhr.send(body);
		});
	}

	/**
	 * Builds an absolute URL from the configured baseUrl and the passed in relative
	 * @param {string} url Relative URL
	 * @returns {string} Absolute url
	 */

	buildUrl(url) {
		if (url[0] === '/') {
			url = this.baseUrl + url;
		}
		return url;
	}

	/**
	 * Get
	 *
	 * Performs an HTTP GET to the specific URL
	 * @param {string} url Url to send to
	 * @returns {Promise} object of the decoded JSON response
	 */
	get(url) {
		return this.request({ method: 'GET', url: url });
	}

	/**
	 * Post
	 *
	 * Performs an HTTP POST to the specific URL
	 * @param {string} url Url to send to
	 * @param {object} data Data to POST
	 * @returns {Promise} object of the decoded JSON response
	 */
	post(url, data) {
		return this.request({ method: 'POST', url: url, data: data });
	}

	/**
	 * Patch
	 *
	 * Performs an HTTP PATCH to the specific URL
	 * @param {string} url Url to send to
	 * @param {object} data Data to PATCH
	 * @returns {Promise} object of the decoded JSON response
	 */
	patch(url, data) {
		return this.request({ method: 'PATCH', url: url, data: data });
	}

	/**
	 * Patch
	 *
	 * Performs an HTTP PUT to the specific URL
	 * @param {string} url Url to send to
	 * @param {object} data Data to PUT
	 * @returns {Promise} object of the decoded JSON response
	 */
	put(url, data) {
		return this.request({ method: 'PUT', url: url, data: data });
	}

	/**
	 * Patch
	 *
	 * Performs an HTTP DELETE to the specific URL
	 * @param {string} url Url to send to
	 * @returns {Promise} object of the decoded JSON response
	 */
	delete(url) {
		return this.request({ method: 'DELETE', url: url });
	}
}

export default new Client();