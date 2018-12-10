# This file uses pytest to test the functionality of each endpoint
# in the app. See http://flask.pocoo.org/docs/1.0/testing/ for details.

import pytest
from src import app as my_app

@pytest.fixture
def client():
    my_app.app.config['TESTING'] = True
    client = my_app.app.test_client()
    yield client

# test for 404 when invalid address given
def test_bad_address(client):
    res = client.get('geocode', query_string='address=~~')
    assert res.status == '404 NOT FOUND'

# test for correct lat/lng given address for Google HQ
def test_good_address(client):
    res = client.get('geocode', query_string='address=1600+amphitheatre+parkway%2C+mountain+view+CA')
    assert res.status == '200 OK'
    assert res.json == {'lat': 37.4227547, 'lng': -122.0857292}
