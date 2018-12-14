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
print(os.environ['DB_CONNECTION'])
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
        body = {
            "message": "User successfully created!"
        }
        return {
            "statusCode": 200,
            "body": json.dumps(body)
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
    (user, session_token) = user_service.login(username, password, session)

    # Server response
    body = {
        "user_id": user.id,
        "displayname": user.name_first + " " + user.name_last,
        "email": user.email,
        "session_token": session_token
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
