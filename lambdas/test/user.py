#!/usr/bin/env python3
import unittest
import json
import handler
from test.util import randstr



class UserTests(unittest.TestCase):


    def test_create_1(self):

        # Creates user dictionary from json
        user_str = '''
        {
          "client_id": 2,
          "username": "willuser",
          "pwd": "theGreatestPassword",
          "name_last": "User",
          "name_first": "Joe",
          "is_enabled": true,
          "email": "willuser@gmail.com",
          "phone": "123-4567",
          "profile_picture_path": "/",
          "timezone_default": "EST",
          "language_default": "English"
        }
        '''

        # Deserializes and makes info unique
        user_dict = json.loads(user_str)
        user_dict['username'] += '_' + randstr()
        user_dict['email'] += '_' + randstr()

        # Invokes handler with payload
        response = handler.user_create(event=user_dict, context=None)

        # Validates response
        print(response)
