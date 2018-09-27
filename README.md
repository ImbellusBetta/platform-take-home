# platform take home
This is a take home project for the Platform team at Imbellus. :rocket:

## Specifications
In this assignment, you will implement a REST API and web UI for a small web app of your design. 

## Getting started
Since your application will use data from Google's Geocode API, you will need a Google account to complete this assignment.
To use this repo you'll need a [github account](https://www.github.com).

### Google Geocoding API key
Obtain an API key from the Google Maps Geocoding API [here](https://developers.google.com/maps/documentation/geocoding/intro).
Here are some instructions on how to do that [here](https://support.google.com/googleapi/answer/6158862?hl=en).

### API
The application should expose the 3 following API endpoints.
1. Geocode
Returns the latitude & longitude of a given address using, for example:

`https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY`

2. Reverse geocode
Returns the address of a given latitude and longitude using, for example:

`https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=YOUR_API_KEY`

3. Geometric distance
Calculates the geometric distance in units of your choice between two lat/long coordinates, and return the distance.
You will need to do this calculation yourself.

### Client
You should create a web client that can call the API. The client can be as simple or complex as you like
using any web technologies from vanilla HTML5, CSS, JS, to your favorite JavaScript framework.

### Extension
We encourage you to get creative and have fun with the assignment. Feel free to extend with more API endpoints, a feature-rich web client, a suite of unit- and end-to-end tests, or more! We encourage you make the server code as robust to exceptions as possible, and treat this portion as if it were production code.

## When you are finished
Please fork this repo and submit a pull request when you are ready to submit it. 
For information or questions please email your primary point of contact, or
write to platform@imbellus.com.

## License
copyright 2018 Imbellus, Inc. All rights reserved.
