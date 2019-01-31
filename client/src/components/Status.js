import React from 'react';
import PropTypes from 'prop-types';
import { Alert } from 'reactstrap';

/**
 * Status uses Bootstrap Alerts to update
 * the status of an API call.
 */
class Status extends React.Component {
	static propTypes = {
		/**
		 * The current loading status
		 */
		status: PropTypes.oneOf(['', 'loading', 'loaded', 'error']).isRequired,
		/**
		 * The success or failure message
		 */
		message: PropTypes.string
	}

	render() {
		return (
			<div>
				{ this.props.status === 'loading' &&
				<Alert color="success">Loading...</Alert>
				}
				{ this.props.status === 'loaded' &&
				<Alert color="primary">Result: { this.props.message }</Alert>
				}
				{ !this.props.status === 'error' &&
				<Alert color="error">Error: { this.props.message }</Alert>
				}
			</div>
		);
	}
}

export default Status;