from flask import Flask, render_template, request, redirect, url_for, session
from geopy.distance import geodesic
import requests
import json


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    # Ensure key has been added.
    if not 'API_key' in session:
        return redirect(url_for('get_key'))
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        # Handle the different redirects that can come from home page.
        # TODO: Refactor to handle this without explicit cases.
        if "convert_lat_long_to_address_button" in request.form:
            return redirect(url_for('take_in_lat_long'))
        elif "convert_address_to_lat_long_button" in request.form:
            return redirect(url_for('take_in_address'))
        elif "calculate_distance_button" in request.form:
            return redirect(url_for('take_in_two_lat_long'))
        elif "logout_button" in request.form:
            return redirect(url_for('logout'))
        else:
            return "You have POSTed with an unsupported form type." + render_template('go_home.html')
    else:
        return "Method not supported on this endpoint! Please POST or GET only." + render_template('go_home.html')


@app.route('/lat_long_to_address/', methods=['GET', 'POST'])
def take_in_lat_long():
    # Handle the case for lat/long coords -> address.
    if not 'API_key' in session:
        return redirect(url_for('get_key'))
    result = ''
    if request.method == 'GET':
        return render_template('lat_long_input.html')
    elif request.method == 'POST':
        if "go_home" in request.form:
            return redirect(url_for('home'))
        # Process lat/long from user and reach out to Google API with this.
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={key}".format(lat=latitude, lng=longitude, key=session['API_key']))
        response_json = json.loads(response.content)
        try:
            # If this is possible, we have a good result. Otherwise, the coordinates are invalid somehow.
            address = response_json['results'][0]['formatted_address']
            header = "The address of latitude {lat} and longitude {lng} is {addr}!<br><h3>Here is a map with a mark for that address:</h3>".format(lat=latitude, lng=longitude, addr=address)
            result = header + render_template('disp_map.html', latitude=latitude, longitude=longitude, address=address, key=session['API_key'])
        except:
            # TODO: Make this more descriptive with actual error.
            result = "The coordinates with Latitude {lat} and Longitude {lng} does not map to an address, sorry!".format(lat=latitude, lng=longitude)
    else:
        result = "Method not supported on this endpoint! Please POST or GET only."
    return result + render_template('go_home.html')

@app.route('/address_to_lat_long/', methods=['GET', 'POST'])
def take_in_address():
    # Handle the case for address -> lat/long coords.
    if not 'API_key' in session:
        return redirect(url_for('get_key'))
    result = ''
    if request.method == 'GET':
        return render_template('address_input.html')
    elif request.method == 'POST':
        if "go_home" in request.form:
            return redirect(url_for('home'))
        # Process address from user and reach out to Google API with this.
        address = request.form['address']
        response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={addr}&key={key}".format(addr=address,key=session['API_key']))
        response_json = json.loads(response.content)
        try:
            # If this is possible, we have a good result. Otherwise, the address is invalid somehow.
            latitude = response_json['results'][0]['geometry']['location']['lat']
            longitude = response_json['results'][0]['geometry']['location']['lng']
            header = "For the address {addr}, the latitude is {lat} and the longitude is {lng}!<br><h3>Here is a map with a mark for that address:</h3>".format(addr=address, lat=latitude, lng=longitude)
            result = header + render_template('disp_map.html', latitude=latitude, longitude=longitude, address=address, key=session['API_key'])
        except:
            # TODO: Make this more descriptive with actual error.
            result = "The address {addr} does not map to latitude and longitude coordinates, sorry!".format(addr=address)
    else:
        result = "Method not supported on this endpoint! Please POST or GET only."
    return result + render_template('go_home.html')

@app.route('/distance_between_two_points/', methods=['GET', 'POST'])
def take_in_two_lat_long():
    # Handle the case for distance between two coordinates.
    if not 'API_key' in session:
        return redirect(url_for('get_key'))
    result = ''
    if request.method == 'GET':
        return render_template('double_lat_long_input.html')
    elif request.method == 'POST':
        if "go_home" in request.form:
            return redirect(url_for('home'))
        # Process both coords from user and reach out to Google API with them.
        latitude1 = request.form['latitude1']
        longitude1 = request.form['longitude1']
        latitude2 = request.form['latitude2']
        longitude2 = request.form['longitude2']
        loc1 = (latitude1, longitude1)
        loc2 = (latitude2, longitude2)
        try:
            # If this is possible, we have a good result. Otherwise, these coords are invalid somehow.
            distance = geodesic(loc1, loc2).miles
            header = "The distance from the point with latitude {lat1} and longitude {lng1} and the point with latitude {lat2} and longitude {lng2} is {dist} miles!<br><h3>Here is what that distance looks like on a map:</h3>".format(lat1=latitude1, lng1=longitude1, lat2=latitude2, lng2=longitude2, dist=distance)
            result = header + render_template('disp_distance_map.html', latitude1=latitude1, longitude1=longitude1, latitude2=latitude2, longitude2=longitude2, key=session['API_key'])
        except:
            # TODO: Make this more descriptive with actual error.
            result = "Error converting the values given to coordinates."
    return result + render_template('go_home.html')


@app.route("/get_key", methods=['GET', 'POST'])
def get_key():
    # Receive the API key to use for this session from this user.
    # TODO: Ensure this is a valid API key before continuing. If not, reprompt.
    if request.method == 'GET':
        return render_template('get_key.html')
    elif request.method == 'POST':
        session['API_key'] = request.form['key']
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    # Remove API Key from this session. This will redirect to home, which will then send
    # back to 'get_key', as the site is structured to always need an API key in the session.
    if not 'API_key' in session:
        return redirect(url_for('get_key'))
    session.pop('API_key', None)
    return redirect(url_for('home'))

app.secret_key = 'YOUR_SECRET_KEY'

