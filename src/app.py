from flask import Flask, make_response, render_template, request, jsonify, session
from math import radians, cos, sin, asin, sqrt
from passwords import GOOGLE_API_KEY
import requests
import json


app = Flask(__name__)

app.config.update(dict(DEBUG=True))

#app.config.from_envvar('FLASK_SETTINGS', silent=True)

# Class version - https://www.codementor.io/codementorteam/how-to-scrape-an-ajax-website-using-python-qw8fuitvi

@app.route('/geocode', methods=['GET'])
def get_geocode():
    address = request.args.get('address')
    if address:
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(
                         address,
                         GOOGLE_API_KEY))
        return json.loads(r.content.decode('utf-8-sig'))
    return make_response('no search param', 401)

'''
@app.route('/reverse', methods=['GET'])
def reverse_geocode():
    data = {}
    data['latlng'] = request.args.get('q', '')
    if data['address']:
        LATLNG = data['latlng']
        #Parse LATLNG and format for API call
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={0}&key={1}'.format(
            LATLNG, GOOGLE_API_KEY))
        #Format returned address the way you want
        new_r = "result"
        return new_r
    return make_response('no search param', 401)

def haversine_distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers.
    return c * r

@app.route('/distance', methods=['GET'])
def distance():
    data = {}
    data['distance'] = request.args.get('a', '')
    if data['distance']:
        lon1, lat1, lon2, lat2 = data['distance'].split()
        return haversine_distance(lon1, lat1, lon2, lat2)
    return make_response('Please enter two lat/long pairs separated by commas', 401)
'''

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
