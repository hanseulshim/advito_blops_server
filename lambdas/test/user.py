#!/usr/bin/env python3
import unittest
from advito.service.user import User, deserialize_user_create
from advito.model import AdvitoUser
from sqlalchemy import create_engine, Column, DateTime, func, Integer, String

class UserTests(unittest.TestCase):

    def setUp():
        self.user_service = UserService()

    def test_create_1(self):

        # Makes session


        # Creates user from json
        user_str = '''
        {
          "client_id": 1,
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
        user_dict = json.loads(usr_str)
        user = deserialize_user_create(user_dict)

        # Inserts user into db




if __name__ == '__main__':
    unittest.main()
