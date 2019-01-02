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

        """
        Runs before tests.
        Creates users.
        """

        # Allocates users
        self.users = []
        self.user_session_tokens = []

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

        # Creates 'n' users and stores them
        n = 3
        for i in range(0, n):
            user = deepcopy(user_template)
            user['username'] += randstr()
            user['email'] += randstr()
            handler.user_create(event=user, context=None)
            self.users.append(user)
            self.user_session_tokens.append(None)



    def test_user_create(self):

        """
        Tests functionality of 'user_create' in handler.
        """

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


    def test_user_login(self):

        """
        Tests functionality of 'user_login' in handler.
        """

        for i in range(0, len(self.users)):

            # Gets user
            user = self.users[i]

            # Creates payload
            event = {
                "username": user['username'],
                "pwd": user['pwd']
            }

            # Invokes
            response = handler.user_login(event=event, context=None)

            # Validates response
            body_dict = json.loads(response['body'])
            apidataset_dict = body_dict['apidataset']
            self.assertEqual(response['statusCode'], 200)
            self.assertEqual (
                apidataset_dict['displayName'],
                user['nameFirst'] + ' ' + user['nameLast']
            )
            self.assertIn('sessionToken', apidataset_dict)


    def test_user_logout(self):

        """
        Tests functionality of 'user_logout' in handler.
        """

        # Logs in a user
        user = self.users[0]
        event = {
            "username": user['username'],
            "pwd": user['pwd']
        }
        response = handler.user_login(event=event, context=None)
        body_dict = json.loads(response['body'])
        session_token = body_dict['apidataset']['sessionToken']

        # Logs out user
        event = { "sessionToken": session_token }
        response = handler.user_logout(event=event, context=None)
        body_dict = json.loads(response['body'])


    def test_dummy_authenticated_endpoint(self):

        """
        Tests functionality of 'dummy_authenticated_endpoint' in handler.
        """

        # For all users created in setUp...
        for user in self.users:

            # Invokes login
            event = {
                "username": user['username'],
                "pwd": user['pwd']
            }
            response = handler.user_login(event=event, context=None)

            # Exctracts value from response
            body_dict = json.loads(response['body'])
            apidataset_dict = body_dict['apidataset']

            # Invokes authenticated endpoint
            event = {
                "sessionToken": apidataset_dict['sessionToken'],
                "payload": "Look at this payload!"
            }
            actual = handler.dummy_authenticated_endpoint(event=event, context=None)

            # Compares expected and actual values
            expected = {'statusCode': 200, 'body': '"Look at this payload!"'}
            self.assertEqual(expected, actual)
