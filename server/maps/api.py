"""
This module contains all the public facing API calls for the maps app
"""

from django.http import JsonResponse
from django.conf import settings
from lib import rest
from . import googlemaps
from .distance import haversine

def config(request):
    """
    Provides map config data to the client
    """
    return JsonResponse({
        'apiKey': settings.MAPS_API_KEY
    })

def search(request):
    """
    Forward Geocode Search API
    Requires an address query string parameter
    """
    address = request.GET.get('address')
    if not address:
        raise rest.RequestException(400, 'parameterMissing', 'Missing required paramer "address"')

    try:
        location = googlemaps.forwardGeocode(request.GET.get('address'))
        return JsonResponse({
            'location': {
                'latitude': location['lat'],
                'longitude': location['lng']
            }
        })
    except googlemaps.GoogleException as e:
        raise rest.RequestException(500, 'upstreamError', e.message, e.debugMessage)

def reverse(request):
    """
    Reverse Geocode Seach API.
    Requires a location query string parameter
    """
    location = request.GET.get('location')
    if not location:
        raise rest.RequestException(400, 'parameterMissing', 'Missing required parameter "location"')
    addresses = googlemaps.reverseGeocode(*location.split(','))
    return JsonResponse({
        'addresses': addresses
    })

def distance(request):
    """
    Calculate the distance between two points API
    Requires location1 and location2 query string parameters

    This function uses the haversine approximate the distance
    between two lat/long coordinates on the earths surface
    """
    location1 = request.GET.get('location1')
    location2 = request.GET.get('location2')
    if not location1 or not location2:
        raise rest.RequestException(400, 'parameterMissing', 'Missing location1/location2 params')

    lat1, lng1, lat2, lng2 = map(float, location1.split(',') + location2.split(','))
    distance = haversine(lat1, lng1, lat2, lng2)

    return JsonResponse({ 'distance': distance })