# Instructions on how to run this locally

This assumes you are running Python3 on a Linux/MacOS machine.
First, make sure you have Flask, requests, and geopy installed through pip

Then, generate your secret code so you can use the Flask sessions feature.
In your terminal, launch a python interface, then type:
```
import os
print(os.urandom(24).hex())
```

Take the result of this and paste it into line 138 of app.py, replacing where it says 'YOUR_SECRET_KEY', but leaving it inside of the single quotes.

Now, in the terminal, cancel out of your Python interface (usually this will be Ctrl+D) and navigate to the Directory containing app.py. Then run the following lines in the terminal:
```
EXPORT FLASK_APP=app.py
flask run
```

This will launch the project locally, and by default you can visit localhost:5000 in your browser to interact with it and test it out. Make sure you have generated an API key using the instructions below to be able to use it well.

# Ideas for Improvement

I was only able to spend a bit of time on this, but there are areas that ideally I would like to flush out more. Some have been marked with TODOs throughout, others are more conceptual. There are two main groups, aesthetic and functional.

## Aesthetic

I realize this is not the prettiest site! I tend to take a more minimal approach but there is room for more. You will notice I avoided JavaScript here, as I prefer sites that load fast and do not personally care about the flair JS can add. This is not to say that it is never appropriate, however, and I think there could be a great discussion about how to incorporate it better here.

## Functional

I am overall happy with the flow and function of the site, but the big area I would spend more time working on is reliability and safety of the code. There is very rudimentary error checking and handling now, but this could be made both much more informative and encompassing with only minor work. One easy one that I would definitely want to do is check if the API key that is given when first accessing the site is valid, and if not reprompt for another. As it is now, the only workaround is to go to the logout page manually after failing the query and trying again - this is clearly not ideal.





# Platform take home
This is a take home project for the Platform team at Imbellus.

## Specifications
In this assignment, you will implement a REST API and web UI for a small web app of your design. 
* The API should be written in python with the packages, framework(s), tools, etc
of your choosing.
* The UI can be a simple design & layout using web technologies of your choice.
* No database is required.
* Include a README with any instructions needed to install and run the
  application.

# Getting started
Since your application will use data from Google's Geocode API, you will need a Google account to complete this assignment.
To use this repo you'll need a [github account](https://www.github.com).

## Google Geocoding API key
Obtain an API key from the Google Maps Geocoding API [here](https://developers.google.com/maps/documentation/geocoding/intro).
Here are some instructions on how to do that [here](https://support.google.com/googleapi/answer/6158862?hl=en).

Google now requires a credit card to register for developer access, but they extend a free credit at registration so no charges are incurred. 

# API
The application should expose 3 endpoints for the following resources:
## Geocode
Geocode: Returns the latitude & longitude of a given address using

`https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY`

## Reverse geocode
Reverse geocode: returns the address of a given latitude and longitude using

`https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=YOUR_API_KEY`

## Geometric distance
Geometric distance: calculates the geometric distance in units of your choice between two lat/long coordinates, and return the distance.
You will need to do this calculation yourself.

# Client
You should create a web client that can call the API. The client can be as simple or complex as you like
using any web technologies from vanilla HTML5, CSS, JS, to your favorite JavaScript framework.

# Extension
We encourage you to get creative and have fun with the assignment. Feel free to extend with more API endpoints, a feature-rich web client, a suite of unit- and end-to-end tests, CI/CD integration or more! We encourage you make the server code as robust to exceptions as possible, and treat this portion as if it were production code.

# When you are finished
Please *fork* this repo and open a pull request to this repo when you are ready to submit the work. 
For information or questions please email your primary point of contact, or
write to platform@imbellus.com.

# License
copyright 2018 Imbellus, Inc. All rights reserved.
