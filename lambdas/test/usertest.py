#!/usr/bin/env python3
import unittest
import json
import handler
from copy import deepcopy
from test.util import randstr



class UserTests(unittest.TestCase):

    """
    Tests all scenarios for users
    """

    def setUp(self):

        # Allocates users
        self.users = []

        # Template for creating users
        user_template = {
          "clientId": 2,
          "username": "user",
          "pwd": "password",
          "nameLast": "Last",
          "nameFirst": "First",
          "email": "user@gmail.com",
          "phone": "123-4567",
          "profile_picture_path": "/",
          "timezoneDefault": "EST",
          "languageDefault": "English"
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
          "clientId": 2,
          "username": "user" + randstr(),
          "pwd": "password",
          "nameLast": "User",
          "nameFirst": "Joe",
          "email": "user@gmail.com" + randstr(),
          "phone": "123-4567",
          "profilePicturePath": "/",
          "timezoneDefault": "EST",
          "languageDefault": "English"
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
            self.assertEqual(actual['statusCode'], 200)
            self.assertEqual (
                apidataset_dict['displayName'],
                user['nameFirst'] + ' ' + user['nameLast']
            )
            self.assertIn('sessionToken', apidataset_dict)
