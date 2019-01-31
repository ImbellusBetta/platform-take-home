"""
This module provides helper methods for accessing Googles
forward and reverse Geocoding APIs

Ensure a valid MAPS_API_KEY is loaded via the secrets file
or these API calls with fail
"""
from django.http import JsonResponse
from django.conf import settings
from lib import rest
import requests

class GoogleException(Exception):
    """ Exception thrown when an error occurs while communicating with Google APIs """

    def __init__(self, message, debugMessage=''):
        self.message = message
        self.debugMessage = debugMessage

def forwardGeocode(address):
    """
    Forward Geocode search with a string of text
    :param address: Human readable address string, single line, csv
    :type address: string
    :returns: A dictionary with latitude/longitude coordinates
    :rtype: dict
    """
    response = googleRequest({ 'address': address })
    return response['results'][0]['geometry']['location']

def reverseGeocode(latitude, longitude):
    """
    Reverse Geocode search with a s

    :param latitude: Latitude
    :param longitude: Longitude
    :type latitude: string, float
    :type longitude: string, float
    :returns: An list of possible addresses
    :rtype: list of str
    """
    response = googleRequest({ 'latlng': str(latitude) + ',' + str(longitude) })
    results = response['results']

    addresses = []
    for result in results:
        addresses.append(result['formatted_address'])

    return addresses

def googleRequest(queryParams):
    """
    Makes an API call to the Google Geocode API

    This function deals with the API key and JSON deserialisation
    throwing a GoogleException if something goes wrong

    :param queryParams: The query string parameters to be sent to the API
    :type queryParams: dict
    :type longitude: string, float
    :returns: A dictionary of deserialised JSON data
    :rtype: dict
    """

    # Setup request with API key
    params = {
        'key': settings.MAPS_API_KEY
    }
    params.update(queryParams)

    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)
    try:
        responseData = response.json()
    except:
        # Failed to load json response, generic error
        raise GoogleException('Fatal Upstream server error')
    if 'error_message' in responseData:
        # Google sent back and error, include it in the debug info
        raise GoogleException('Fatal Upstream server error', responseData['error_message'])

    return responseData
