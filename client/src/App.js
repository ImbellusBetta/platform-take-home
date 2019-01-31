import React from 'react';
import { BrowserRouter, Route, Redirect } from 'react-router-dom';
import Nav from 'components/Nav';
import Geocode from 'containers/Geocode';
import Distance from 'containers/Distance';

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

/**
 * App Entry Points
 *
 * Defines routes to containers based on urls
 */
class App extends React.Component {
	render() {
		return (
			<BrowserRouter>
				<Nav>
					<div className="content">
						<Route exact path="/" component={Home}/>
						<Route exact path="/geocode" component={Geocode} />
						<Route exact path="/distance" component={Distance} />
					</div>
				</Nav>
			</BrowserRouter>
		);
	}
}

class Home extends React.Component {
	render() {
		return <Redirect to="/geocode"/>;
	}
}

export default App;
