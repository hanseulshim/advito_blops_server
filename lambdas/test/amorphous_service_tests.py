#!/usr/bin/env python3
import unittest
import json
import handler
from copy import deepcopy
from test.util import randstr



class AmorphousServiceTests(unittest.TestCase):

    """
    Tests all scenarios for users
    """

    def setUp(self):
        pass



    def test_udf_story_air(self):
        event = {
            'clientId' : 1
        }
        result = handler.udf_story_air(event=event, context=None)
        body = json.dumps(result['body'])
        self.assertEqual(result['statusCode'], 200)
        self.assertIn('udf_story_air', body)
