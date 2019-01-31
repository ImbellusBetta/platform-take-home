"""
API Tests for the Maps Module
"""
from django.test import TestCase
from lib.test import client

class MapsTest(TestCase):

    def testValidAddress(self):
        """ Test forward geocode """
        result = client.get('/maps/geocode/search?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA')
        self.assertEqual(int(result['location']['latitude']), 37)
        self.assertEqual(int(result['location']['longitude']), -122)

    def testInvalidAddress(self):
        """ Test forward geocode without supplying required parameter """
        result = client.get('/maps/geocode/search')
        self.assertEqual(result['error'], 'parameterMissing')

    def testLatitudeLongitude(self):
        """ Test reverse geocode """
        result = client.get('/maps/geocode/reverse?location=40.714224,-73.961452')
        self.assertTrue(len(result['addresses'][0]) > 0)

    def testDistance(self):
        """ Test distance between two points """
        result = client.get('/maps/distance')
        self.assertTrue('error' in result)
        result = client.get('/maps/distance/calculate?location1=0,0&location2=1,1')
        self.assertEqual(int(result['distance']), 157)

    def testConfig(self):
        result = client.get('/maps/config')
        self.assertTrue('apiKey' in result)

