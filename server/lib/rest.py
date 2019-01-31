"""
This module provides a Django Middleware to
simplify writing REST style interfaces inside
the Django Framework
"""
import traceback
import json
import sys

from django.conf import settings
from django.utils import timezone
from django.http import JsonResponse, HttpResponse

class RequestException(Exception):
    """
    This exception can be thrown anywhere inside Django view code
    to abort the API call and return a standardized, meaningful error
    """

    def __init__(self, status, error, message, debugMessage=None):
        """
        :param status: The HTTP status code to return
        :param error: The computer friendly error string to return. eg, parameterMissing, internalError, etc
        :param message: The human readable error message
        :param debugMessage: Extra info, only sent if debug is enabled
        :type status: int
        :type error: string
        :type message: string
        :type debugMessage: string
        """
        self.status = status
        self.error = error
        self.message = message
        self.debugMessage = debugMessage

    def __str__(self):
        return self.message

class Middleware(object):
    """
    Middleware class that must be added to your Apps middleware definition
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Decode body data for POST, PUT and PATCH
        if request.method in ['POST', 'PUT', 'PATCH'] and len(request.body) > 0:
            request.json = json.loads(request.body.decode('utf-8'))
        else:
            request.json = {}

        # Executable the standard Django view
        response = self.get_response(request)
        if not isinstance(response, JsonResponse) and response.status_code != 200:
            response = JsonResponse({ 'error': 'internalError', 'message': str(response.content) }, status=response.status_code)

        # Set no cache header if one hasn't been set
        response.setdefault('Cache-Control', 'no-cache')
        return response

    def process_exception(self, request, exception):
        # If this one of our exceptions, format it
        if isinstance(exception, RequestException):
            result = { 'error': exception.error, 'message': exception.message }
            if exception.debugMessage and settings.DEBUG:
                result['debug'] = exception.debugMessage
            return JsonResponse(result, status=exception.status)

        else:
            # Generic exception, do our best, include exception message in
            # debug info if we're in debug mode
            traceback.print_exc()
            result = { 'error': 'internalError', 'message': 'Internal Error' }
            if settings.DEBUG:
                result['debug'] = exception.message
            return JsonResponse(result, status=500)

