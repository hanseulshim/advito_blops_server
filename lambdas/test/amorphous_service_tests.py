#!/usr/bin/env python3
import unittest
import json
import handler
from copy import deepcopy
from test.util import randstr



class AmorphousServiceTests(unittest.TestCase):

    """
    Tests all scenarios for amorphous data.
    """

    def test_udf_story_air(self):
        event = {'clientId' : 1}
        result = handler.udf_story_air(event=event, context=None)
        body = json.dumps(result['body'])
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('udf_story_air', body)


    def test_udf_story_air_traffic(self):
        event = {'clientId' : 1}
        result = handler.udf_story_air_traffic(event=event, context=None)
        body = json.dumps(result['body'])
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('udf_story_air_traffic', body)
