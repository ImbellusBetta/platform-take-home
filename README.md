# Geocoder

## About

Geocoder provides an interface for Google's Geocode API, exposing the
following 4 API endpoints:

1. `/geocode`

Geocode: Returns the latitude & longitude of a given address.

2. `/reverse`

Reverse geocode: Returns the address of a given latitude and longitude using.

3. `/geodistance`

Geodistance: Calculates the great circle distance in kilometers between 
two lat/long coordinates.

4. `/address_geodistance`

Address Geodistance: Extends `/geodistance` to calculate the great circle distance
in kilometers between two locations.

## Install & Setup

You will need Python 3.0 or greater, as well as Flask, which you can install
with pip: 

```python
pip install flask
```

You will also need to obtain a Google API key,

Once you have this key, create a file called `passwords.py`,
add your Google API key to it by assigning it as a variable 
(`GOOGLE_API_KEY = your_key`), and place this file in the `geocoder` folder.

To run the app locally, open your terminal of choice, `cd` into `geocoder`,
and run `python app.py` on the command line.

Unittests require pytest, which you can also install with pip:

```python
pip install pytest
```
To run tests, `cd` into the root, and run `pytest` on the command line. 
