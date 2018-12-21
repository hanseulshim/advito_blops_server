#!/usr/bin/env python3
import unittest
import json
import handler
from copy import deepcopy
from test.util import randstr



class UserTests(unittest.TestCase):


    def setUp(self):

        # Allocates users
        self.users = []

        # Template for creating users
        user_template = {
          "client_id": 2,
          "username": "user",
          "pwd": "password",
          "name_last": "Last",
          "name_first": "First",
          "email": "user@gmail.com",
          "phone": "123-4567",
          "profile_picture_path": "/",
          "timezone_default": "EST",
          "language_default": "English"
        }

        # Creates 'n' users and stores users
        n = 3
        for i in range(0, n):
            user = deepcopy(user_template)
            user['username'] += randstr()
            user['email'] += randstr()
            handler.user_create(event=deepcopy(user), context=None)
            self.users.append(user)



    def test_create_1(self):

        # Creates event
        event = {
          "client_id": 2,
          "username": "willuser" + randstr(),
          "pwd": "theGreatestPassword",
          "name_last": "User",
          "name_first": "Joe",
          "email": "willuser@gmail.com" + randstr(),
          "phone": "123-4567",
          "profile_picture_path": "/",
          "timezone_default": "EST",
          "language_default": "English"
        }

        # Generates expected value
        expected = {
            'statusCode': 200,
            'body': '{"success": true, "apicode": "OK", "apimessage": "User successfully created.", "apidataset": {"message": "User successfully created!"}}'
        }

        # Invokes
        actual = handler.user_create(event=event, context=None)

        # Validates response
        self.assertEqual(expected, actual)


    def test_login_1(self):

        for user in self.users:

            # Creates payload
            event = {
                "username": user['username'],
                "pwd": user['pwd']
            }

            # Invokes
            actual = handler.user_login(event=event, context=None)

            # Validates response
            body_dict = json.loads(actual['body'])
            apidataset_dict = body_dict['apidataset']
            self.assertEquals(actual['statusCode'], 200)
            self.assertEquals (
                apidataset_dict['displayName'],
                user['name_first'] + ' ' + user['name_last']
            )
            self.assertIn('sessionToken', apidataset_dict)
