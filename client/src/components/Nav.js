import React from 'react';
import { Link } from 'react-router-dom';
import { Collapse, Navbar, NavbarToggler, NavbarBrand, Nav, NavItem, NavLink } from 'reactstrap';

/**
 * Top level navigation bar.
 *
 * Implements a logo and a few simple clickable links to access the different
 * parts of the application
 */
class NavComponent extends React.Component {

	constructor(props) {
		super(props);
		this.toggleNavbar = this.toggleNavbar.bind(this);
		this.state = {
			isOpen: false
		};
	}

	toggleNavbar() {
		this.setState({
			isOpen: !this.state.isOpen
		});
	}

	render() {
		return (
			<div>
				<Navbar color="dark" dark expand="md">
					<NavbarBrand href="/">
						<img style={{ width: '32px', height: '32px' }} src="/logo.png" alt="logo" />
					</NavbarBrand>
					<NavbarToggler onClick={this.toggleNavbar} />
					<Collapse isOpen={this.state.isOpen} navbar>
						<Nav navbar>
							<NavItem>
								<NavLink tag={Link} to="/geocode">Geocode</NavLink>
							</NavItem>
							<NavItem>
								<NavLink tag={Link} to="/distance">Distance</NavLink>
							</NavItem>
						</Nav>
					</Collapse>
				</Navbar>
				<div>
					{this.props.children}
				</div>
			</div>
		);
	}
}

export default NavComponent;
