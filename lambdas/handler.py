import json
import urllib.parse
import base64
import secrets
import hashlib
import boto3
import os
import traceback
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import advito.util
from advito.service.user import UserService, deserialize_user_create
from advito.error import AdvitoError, LoginError

# Unpacks environment variables to build DB client and services
session_duration_sec = int(os.environ['SESSION_DURATION_SEC'])
db_connection = os.environ['DB_CONNECTION']

# Creates SQLAlchemy DB client
engine = create_engine(db_connection)

# Creates services that control business logic
user_service = UserService(session_duration_sec)


################# Util function ###################
def error_handle(lambda_func):

    def wrapper(event, context):

        # Creates session
        session = Session(engine)
        try:
            body = lambda_func(event, context, session)
            session.commit()
            status_code = 200

        except (LoginError, IntegrityError) as e:
            session.rollback()
            body = {
                "success": False,
                "apicode": "NOT FOUND",
                "apimessage": "Could not log in user. Ensure that username and email are unique.",
                "apidataset": None
            }
            status_code = 400
            traceback.print_exc()

        except AdvitoError as e:
            session.rollback()
            body = {
                "success": False,
                "apicode": "BAD",
                "apimessage": str(e),
                "apidataset": None
            }
            status_code = 400
            traceback.print_exc()

        except Exception as e:
            print(type(e))
            session.rollback()
            body = {
                "success": False,
                "apicode": "ERROR",
                "apimessage": "Unexpected exception occurred.",
                "apidataset": None
            }
            status_code = 500
            traceback.print_exc()

        finally:
            session.close()

        # Jsonifies response and sends response
        return {
            "statusCode": status_code,
            "body": json.dumps(body)
        }

    # Sends decorated
    return wrapper



###################### Handlers go here ###########################

@error_handle
def user_create(event, context, session):

    """
    Reads a user from the event body and inserts it into the database.
    :param event: User JSON as a dict.
    :param context: AWS context.
    """

    # Deserializes user from json, inserts and commits
    user_create_json = event
    user = deserialize_user_create(user_create_json)
    user_service.create(user, session)

    # Server response
    body = {
        "message": "User successfully created!"
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }


@error_handle
def user_login(event, context, session):

    """
    Logs in a user.
    :param event: Login JSON as a dict.
    :context: AWS context
    """

    # Acquires username and password
    login_json = event
    username = login_json['username']
    password = login_json['pwd']

    # Tries to login
    (user, user_session) = user_service.login(username, password, session)
    session.commit()

    # Server response
    body = {
        "user_id": user.id,
        "displayname": user.name_first + " " + user.name_last,
        "email": user.email,
        "session_token": user_session.session_token
    }
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
