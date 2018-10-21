from flask import Flask, make_response, render_template, request, jsonify, session
from math import radians, cos, sin, asin, sqrt
from geocoder.passwords import GOOGLE_API_KEY
import requests
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)
app.config.update(dict(DEBUG=True))

@app.route('/geocode', methods=['GET'])
def geocode():
    address = request.args.get('address')
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
    if address:
        try:
            r = requests.get(URL.format(address, GOOGLE_API_KEY))
        except OSError:
            return make_response(jsonify({"OSError" : "Network not availble."}))

        content = r.json()
        if content['status'] == 'OK':
            res = content['results'][0]['geometry']['location']
            vals = [str(val) for val in res.values()]
            res_map = {"latlng": " ".join(vals)}
            final_res = jsonify(res_map)
            return make_response(final_res)
        elif content['status'] != 'UNKNOWN_ERROR':
            return make_response(jsonify({'error': content['status']}))

    return make_response(jsonify({'error':'Please provide search params'}), 401)

@app.route('/reverse', methods=['GET'])
def reverse_geocode():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}'
    if lat and lng:
        try:
            r = requests.get(URL.format(lat, lng, GOOGLE_API_KEY))
        except OSError:
            return make_response(jsonify({"OSError" : "Network not available"}))

        content = r.json()
        if content['status'] == 'OK':
            res = {"address": content['results'][0]['formatted_address']}
            final_res = jsonify(res)
            return make_response(final_res)
        elif content['status'] != 'UNKNOWN_ERROR':
            return make_response(jsonify({'error': content['status']}))

    return make_response(jsonify({'error':'Please provide search params'}), 401)

def haversine_distance(lng1, lat1, lng2, lat2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])

    # haversine formula
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers.
    return round(c * r, 3)

@app.route('/geodistance', methods=['GET'])
def calculate_geodistance():
    lat1 = request.args.get('lat1')
    lng1 = request.args.get('lng1')
    lat2 = request.args.get('lat2')
    lng2 = request.args.get('lng2')

    if lat1 and lng1 and lat2 and lng2:
        res = {'geodistance': haversine_distance(
                  float(lng1),
                  float(lat1),
                  float(lng2),
                  float(lat2))}

        final_res = jsonify(res)
        return make_response(final_res)
    return make_response(jsonify({'error':'Please provide search params'}), 401)

@app.route('/address_geodistance', methods=['GET'])
def calculate_address_geodistance():
    address1 = request.args.get('address1')
    address2 = request.args.get('address2')
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'

    def generate_latlng(address):
        try:
            a = requests.get(URL.format(address, GOOGLE_API_KEY))
        except OSError:
            pass
        content = a.json()
        if content['status'] == 'OK':
            res = content['results'][0]['geometry']['location']
            return [val for val in res.values()]
        elif content['status'] != 'UNKNOWN_ERROR':
            return make_response(jsonify({'error': content['status']}))

    if address1 and address2:
        lat1, lng1 = generate_latlng(address1)
        lat2, lng2 = generate_latlng(address2)

        res = {'address_geodistance': haversine_distance(
                  float(lng1),
                  float(lat1),
                  float(lng2),
                  float(lat2))}

        final_res = jsonify(res)
        return make_response(final_res)
    return make_response(jsonify({'error':'Please provide search params'}), 401)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
