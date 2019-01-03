import json
import urllib.parse
import base64
import secrets
import hashlib
import os
import traceback
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import advito.util
from advito.service.user import UserService, deserialize_user_create
from advito.service.amorphous import AmorphousService
from advito.error import AdvitoError, LogoutError, LoginError, BadRequestError, InvalidSessionError, ExpiredSessionError


# Unpacks environment variables to build DB client and services
session_duration_sec = int(os.environ['SESSION_DURATION_SEC'])
db_connection = os.environ['DB_CONNECTION']

# Creates SQLAlchemy DB client
engine = create_engine(db_connection)

# Creates services that control business logic
user_service = UserService(session_duration_sec)
amorphous_service = AmorphousService()

################ Decorators ##################
def handler_decorator(func):


    """
    Decorates a handler function by supplying it with a SQLAlchemy session object.
    Includes error-handling code in the event that an Exception is thrown.
    :param func: Handler function to be decorated. Function should expect an AWS event, an AWS context and an SQLAlchemy session.
    :return: Decorated version of handler function supplied.
    """

    def wrapper(event, context):

        # Creates session
        session = Session(engine)

        # Runs underlying funtion.
        # Performs error handling in the event of an Exception being raised.
        try:
            body = func(event, context, session)
            session.commit()
            status_code = 200

        except (LoginError, LogoutError) as e:
            session.rollback()
            body = {
                "success": False,
                "apicode": "NOT FOUND",
                "apimessage": str(e),
                "apidataset": None
            }
            status_code = 400

        except InvalidSessionError as e:
            session.rollback()
            body = {
                "success": False,
                "apicode": "INVALID",
                "apimessage": str(e),
                "apidataset": None
            }
            status_code = 400


        except IntegrityError as e:
            session.rollback()
            body = {
                "success": False,
                "apicode": "INVALID",
                "apimessage": "Database rejected update/insert.",
                "apidataset": None
            }
            status_code = 400

        except ExpiredSessionError as e:
            session.rollback()
            body = {
                "success": False,
                "apicode": "EXPIRED",
                "apimessage": str(e),
                "apidataset": None
            }
            status_code = 400

        except BadRequestError as e:
            session.rollback()
            body = {
                "success": False,
                "apicode": "BAD",
                "apimessage": str(e),
                "apidataset": None
            }
            status_code = 400

        except Exception as e:
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

        # Jsonifies response and sends it
        return {
            "statusCode": status_code,
            "body": json.dumps(body)
        }

    # Returns decorated function
    return wrapper


def authenticate_decorator(func):

    """
    Decorates a function such that it checks that the token in the request exists in the database and is not expired.
    After the check, it invokes the underlying function
    """

    def wrapper(event, context, session):

        # Validates that user is logged in
        session_token = event["sessionToken"]
        payload = event["payload"]
        user_service.validate_logged_in(session_token, session)

        # Invokes underlying function
        return func(event, context, session)

    # Returns decorated function
    return wrapper



###################### Handlers ###########################

@handler_decorator
def user_create(event, context, session):

    """
    Reads a user from the event body and inserts it into the database.
    :param event: User JSON as a dict.
    :param context: AWS context.
    :param session: Session used for database connectivity.
    """

    # Deserializes user from json, inserts and commits
    user = deserialize_user_create(event)
    user_service.create(user, session)

    # Creates response and returns it
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully created.",
        "apidataset": {
            "message": "User successfully created!"
        }
    }


@handler_decorator
def user_login(event, context, session):

    """
    Logs in a user.
    :param event: Login JSON as a dict.
    :param context: AWS context.
    :param session: Session used for database connectivity.
    """

    # Acquires username and password
    login_json = event
    username = login_json['username']
    password = login_json['pwd']

    # Tries to login
    (user, user_session) = user_service.login(username, password, session)
    session.commit()

    # Creates response and returns it
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully logged in.",
        "apidataset": {
            "displayName": user.name_first + " " + user.name_last,
            "clientId": user.client_id,
            "profilePicturePath": user.profile_picture_path,
            "sessionToken": user_session.session_token
        }
    }


@handler_decorator
def user_logout(event, context, session):

    """
    Logs out a user.
    :param event: Login JSON as a dict.
    :param context: AWS context.
    :param session: Session used for database connectivity.
    """

    # Acquires session info
    logout_json = event
    session_token = logout_json['sessionToken']
    user_service.logout(session_token, session)
    session.commit()

    # Creates response and returns it
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully logged out.",
        "apidataset": None
    }

@handler_decorator
@authenticate_decorator
def dummy_authenticated_endpoint(event, context, session):
    payload = event["payload"]
    return payload


@handler_decorator
@authenticate_decorator
def udf_story_air(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_air(client_id, session)
    return result
