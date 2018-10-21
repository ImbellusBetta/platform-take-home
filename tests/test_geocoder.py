import pytest

from geocoder import app as geocoder_app

@pytest.fixture
def client():
    geocoder_app.app.config['TESTING'] = True
    client = geocoder_app.app.test_client()
    yield client

# Geocode
def test_no_params_geocode(client):
    r = client.get('/geocode')
    assert '401 UNAUTHORIZED' == r.status

def test_json_geocode1(client):
    r = client.get('/geocode', query_string='address=Paris, France')
    assert b'{\n  "latlng": "48.856614 2.3522219"\n}' == r.data

def test_json_geocode2(client):
    r = client.get('/geocode', query_string='address=Paris, Texas')
    assert b'{\n  "latlng": "48.856614 2.3522219"\n}' != r.data

# Reverse
def test_no_params_reverse(client):
    r = client.get('/reverse')
    assert '401 UNAUTHORIZED' == r.status

def test_json_reverse(client):
    r = client.get('/reverse', query_string='lat=33.6609389+&lng=-95.55551299999999')
    assert b'{\n  "address": "37 Clarksville St, Paris, TX 75460, USA"\n}' == r.data

# Geodistance
def test_no_params_geodistance(client):
    r = client.get('/geodistance')
    assert '401 UNAUTHORIZED' == r.status

def test_json_geodistance(client):
    r = client.get('/geodistance',
                   query_string='lat1=48.856614+&lng1=2.3522219&lat2=33.6609389+&lng2=-95.55551299999999')
    assert b'{\n  "geodistance": 7783.341\n}' == r.data

# Address Geodistance
def test_no_params_address_geodistance(client):
    r = client.get('/address_geodistance')
    print("R:", r)
    assert '401 UNAUTHORIZED' == r.status

def test_json_address_geodistance(client):
    r = client.get('/address_geodistance',
                   query_string='address1=Paris+Texas&address2=Paris+France')
    assert b'{\n  "address_geodistance": 7783.341\n}' == r.data
