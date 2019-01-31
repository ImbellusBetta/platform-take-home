# Geocode Project

This repo contains a working example of a client/server architecture that performs Geocode lookups as well as simple Haversine distance calculation between two points.

The client makes REST API calls to the the server, which uses Google Place to lookup coordinates which it returns to the client. The client also integrates with Google Maps to display these locations on a world map.

Both the Server and Client projects provide test suites for checking the REST API and browser interfaces are fully functional.

### Server Setup (Python)
1. Create a new Python3 virtual env and activate it
1. Create a file called *mapsapikey.txt* in the server/config folder and place your Google Maps API key in it
1. Switch to the *server* folder and use pip to install the requirments ```pip install -r requirements.txt```
1. Test the api: ```python manage.py test```
1. Run the api ```python manage.py runserver```

### Client Setup (React)
1. Install NodeJS and the YARN package manager (```npm install -g yarn```)
1. Switch to the *client* folder and install the required packages ```yarn install```
1. Run the client ```yarn start```, this should launch the browser and allow you to use the interface (ensure the backend is running!)
1. Test the interface - Ensure the backend and frontend are already running, then in a third window switch to the *client* folder and execute ```yarn test```
