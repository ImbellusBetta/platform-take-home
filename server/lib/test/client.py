"""
Helper methods for testing API calls
"""
import json
from django.test.client import Client

client = Client()

def get(url):
    """
    Performs and HTTP GET and returns the result as a dict
    :param url: The URL to request
    :type url: str
    :returns: dict of deserialized json data
    :rtype: dict
    """
    response = client.get(url)
    return parseResponse(response)

def parseResponse(response):
    """
    Deserialised a dict from a requests response object
    :param response: The requests Response object
    :type response: requests.Response
    :returns: dict of deserialized json data
    :rtype: dict
    """

    # If its streaming, we need to read it in bit by bit
    if hasattr(response, 'streaming_content'):
        data = ''
        for s in response.streaming_content:
            data += s.decode('utf-8')
    else:
        data = response.content.decode('utf-8')
    return json.loads(data)


__all__ = ['get']

