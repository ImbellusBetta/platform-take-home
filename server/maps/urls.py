"""
Interal URL mappings for the Maps Module
"""
from django.conf.urls import url

from . import api

urlpatterns = [
	url(r'^config$', api.config),
	url(r'^geocode/search$', api.search),
	url(r'^geocode/reverse$', api.reverse),
	url(r'^distance/calculate$', api.distance)
]