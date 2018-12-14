import json
import urllib.parse
import base64
import secrets
import hashlib
import boto3
import os
from datetime import datetime

# SQLAlchemy
from sqlalchemy import create_engine, Column, DateTime, func, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# Advito
import advito.util
from advito.service.user import UserService, deserialize_user_create



# Creates dependencies
engine = create_engine(os.environ['DB_CONNECTION']) # DB Client
user_service = UserService()                        # User Service


###################### Handlers go here ###########################

def user_create(event, context):

    """
    Reads a user from the event body and inserts it into the database.
    :param event: User JSON as a dict.
    :param context: AWS context.
    """

    # With session...
    session = Session(engine)
    try:

        # Deserializes user from json, inserts and commits
        user_create_json = event
        user = deserialize_user_create(user_create_json)
        user_service.create(user, session)
        session.commit()

        # Server response
        return {
            "statusCode": 200,
            "body": {
                "message": "User successfully created!"
            }
        }

    # Handle failure
    except:
        session.rollback()
        raise


def user_login(event, context):

    """
    Logs in a user.
    :param event: Login JSON as a dict.
    :context: AWS context
    """

    # Creates session. No try-catch logic because nothing is inserted.
    session = Session(engine)

    # Acquires username and password
    login_json = event
    username = login_json['username']
    password = login_json['pwd']

    # Tries to login
    login_token = user_service.login(username, password, session)

    # Server response
    return {
        "statusCode": 200,
        "body": {
            "message": "Successfully logged in!",
            "token": login_token
        }
    }









def hello(event, context):

    #util.saltHashTuple = util.saltHash('Password1', '')
    #util.saltHashPwd = util.saltHashTuple[0]
    #salt = util.saltHashTuple[1]
    #print('Hashed Password = ' + util.saltHashPwd)
    #print('salt = ' + salt)

    #usr = advito_user(id=2, client_id=1, username='joeuser', pwd=util.saltHashPwd, name_last='User', name_first='Joe',
    #  is_enabled=True, must_change_pwd=False, pwd_expiration='01/01/2024', email='joeuser@gmail.com',
    #  phone='123-4567', profile_picture_path='/', timezone_default='EST', language_default='English', user_salt=salt,
    #  created='01/01/1900', modified='12/12/2018')
    #session.add(usr)
    #session.commit()

    #salt = 'rB/YTF0DENZhZiPV9cpaeg=='
    username = event['username']
    password = event['password']

    user_is_enabled = False
    user_id = 0
    user_email = ''
    user_displayname = ''
    user_token = 'abc'
    salt = ''

    for row in session.query(advito_user).filter(advito_user.username==username):
      salt = row.user_salt
      user_is_enabled = row.is_enabled
      user_id = row.id
      user_email = row.email
      user_displayname = row.name_first + " " + row.name_last
      user_pwd = row.pwd

    print('salt = ' + salt)
    util.saltHashTuple = util.saltHash(password, salt)
    util.saltHashPwd = util.saltHashTuple[0]
    salt = util.saltHashTuple[1]
    print('Hashed Password = ' + util.saltHashPwd)
    print('user_pwd = ' + user_pwd)

    #for row in session.query(advito_user).filter(advito_user.username==username, advito_user.pwd==util.saltHashPwd):
    #  print(row.id, row.name_first, row.name_last, row.email,  row.is_enabled)
    #  user_is_enabled = row.is_enabled
    #  user_id = row.id
    #  user_email = row.email
    #  user_displayname = row.name_first + " " + row.name_last

    # Print the column names of each table.
    #for table in Base.metadata.sorted_tables:
    #  print(table.name)
    #  for column in table.columns:
    #    print(column)

    for row in session.query(advito_user_session).filter(advito_user_session.advito_user_id==user_id):
      print('session_token = ' + row.session_token)
      user_token = row.session_token

    response = {
        "statusCode": 200,
        "user_id": user_id,
        "displayname": user_displayname,
        "email": user_email,
        "session_token": user_token
    }

    return response
