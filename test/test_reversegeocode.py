# This file uses pytest to test the functionality of each endpoint
# in the app. See http://flask.pocoo.org/docs/1.0/testing/ for details.

import pytest
from src import app as my_app

@pytest.fixture
def client():
    my_app.app.config['TESTING'] = True
    client = my_app.app.test_client()
    yield client

# test for correct address given lat/lng
def test_good_latlng(client):
    res = client.get('reversegeocode', query_string='lat=37.7991&lng=-122.4213')
    assert res.status == '200 OK'
    assert res.json == '1330 Union St, San Francisco, CA 94109, USA'

# test for result not found given lat lng to nowhere
def test_bad_latlng(client):
    res = client.get('reversegeocode', query_string='lat=0&lng=0')
    assert res.status == '404 NOT FOUND'

# test for bad request given non numeric lat lng
def test_invalid_latlng(client):
    res = client.get('reversegeocode', query_string='lat=abc&lng=z')
    assert res.status == '400 BAD REQUEST'
