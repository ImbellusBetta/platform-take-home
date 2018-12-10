# This file uses pytest to test the functionality of each endpoint
# in the app. See http://flask.pocoo.org/docs/1.0/testing/ for details.

import pytest
from simplegeo import app as my_app

@pytest.fixture
def client():
    my_app.app.config['TESTING'] = True
    client = my_app.app.test_client()
    yield client

# test for correct distance given coordinates
def test_good_distance_calc(client):
    res = client.get('distance', query_string='lat1=37&lng1=-122&lat2=37.1&lng2=-122&unit=mi')
    assert res.json == {'distance': 6.909341954924607}

# test for 400 given invalid lat/lng
def test_invalid_distance_params(client):
    res = client.get('distance', query_string='lat1=a&lng1=03&lat2=12&lng2=23&unit=mi')
    assert res.status == '400 BAD REQUEST'

# test for correct distance given same coordinates and km
def test_km_good_distance_calc(client):
    res = client.get('distance', query_string='lat1=37&lng1=-122&lat2=37.1&lng2=-122&unit=km')
    assert res.json == {'distance': 11.119508023353307}
