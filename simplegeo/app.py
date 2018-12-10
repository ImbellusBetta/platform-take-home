from flask import Flask, render_template, request, make_response, jsonify
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
import requests
import json
from haversine import haversine

# constants - geocoding endpoint & API key (replace this with your API key, should be secret)
GEOCODE_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
API_KEY = 'AIzaSyC_G8IdhaEqWEkXrlKHBtkFtSr6zonMnS4'

# setup app with Bootstrap & Navbar
app = Flask(__name__)
Bootstrap(app)
nav = Nav(app)

# create top navigation bar to move throughout web app
@nav.navigation('navbar')
def create_navbar():
    home_view = View('Home', 'home')
    help_view = View('Help', 'help')
    return Navbar('SimpleGeo', home_view, help_view)

# home page
@app.route('/')
def home():
    return render_template('home.html')

# short about page with list of capabilities of app
@app.route('/help')
def help():
    return render_template('help.html')

# pull address from query param, and call endpoint to get lat/lon
@app.route('/geocode', methods=['GET'])
def geocode():
    address = request.args.get('address')
    params = {'address': address,'key': API_KEY}
    # try to call geocode API, return failures if call fails
    try:
        req = requests.get(GEOCODE_API_URL, params=params)
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'Error' : http_err})
    except requests.exceptions.RequestException as err:
        return jsonify({'Error' : err})

    # parse response and return appropriate response
    res = req.json()
    if res['status'] == 'OK':
        latlong = res['results'][0]['geometry']['location']
    else:
        return make_response(jsonify({'Error' : res['status']}), 404)

    return jsonify(latlong)

# pull latlng from query param, and call endpoint to get address
@app.route('/reversegeocode', methods=['GET'])
def reversegeocode():
    # something must be passed, check to make sure it is an int
    try:
        float(request.args.get('lat'))
        float(request.args.get('lng'))
    except ValueError:
        return make_response(jsonify({'Error' : 'BAD REQUEST'}), 400)

    params = {'latlng': request.args.get('lat') + ',' + request.args.get('lng'),
              'key': API_KEY
             }
    try:
        req = requests.get(GEOCODE_API_URL, params=params)
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'Error' : http_err})
    except requests.exceptions.RequestException as err:
        return jsonify({'Error' : err})

    # parse response and give appropriate response
    res = req.json()
    if res['status'] == 'OK':
        address = res['results'][0]['formatted_address']
    else:
        return make_response(jsonify({'Error' : res['status']}), 404)

    return jsonify(address)

# calculate haversine distance using python module haversine
@app.route('/distance', methods=['GET'])
def distance():
    # ensure only numbers are passed into request
    try:
        lat1 = float(request.args.get('lat1'))
        lat2 = float(request.args.get('lat2'))
        lng1 = float(request.args.get('lng1'))
        lng2 = float(request.args.get('lng2'))
    except ValueError:
        return make_response(jsonify({'Error' : 'BAD REQUEST'}), 400)

    start = (float(lat1),float(lng1))
    dest = (float(lat2),float(lng2))
    # ensure numbers are in appropriate range for lat/lng
    if not -90 <= start[0] <= 90 or not -90 <= dest[0] <= 90:
        return make_response(jsonify({'Error' : 'Latitude must be between -90 and 90 degrees'}), 400)
    if not -180 <= start[1] <= 180 or not -180 <= dest[1] <= 180:
        return make_response(jsonify({'Error' : 'Longitude must be between -180 and 180 degrees'}), 400)
    dist = haversine(start, dest, unit=request.args.get('unit'))
    return jsonify({'distance': dist})


if __name__ == '__main__':
  app.run(debug=True)
