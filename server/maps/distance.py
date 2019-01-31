"""
This module implements methods for calculating distances
"""
import math

def haversine(lat1, lng1, lat2, lng2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees) using the haversine
    formula - https://en.wikipedia.org/wiki/Haversine_formula

    :param lat1: Latitude of point1
    :param lng1: Longitude of point1
    :param lat2: Latitude of point2
    :param lng2: Longitude of point2
    :type lat1: str, float
    :type lng1: str, float
    :type lat2: str, float
    :type lng2: str, float
    :returns: Approximate distance in KM between the two points
    :rtype: float

    """
    # convert decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2])

    # haversine formula
    dlat = lat2 - lat1
    dlon = lng2 - lng1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371 # Radius of earth in kilometers.
    return c * r