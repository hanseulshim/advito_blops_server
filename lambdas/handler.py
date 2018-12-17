import json
import urllib.parse
import base64
import secrets
import hashlib
import boto3
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import advito.util
from advito.service.user import UserService, deserialize_user_create

# Unpacks environment variables to build DB client and services
session_duration_sec = int(os.environ['SESSION_DURATION_SEC'])
db_connection = os.environ['DB_CONNECTION']

# Creates SQLAlchemy DB client
engine = create_engine(db_connection)

# Creates services that control business logic
user_service = UserService(session_duration_sec)


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

        # Commits results
        try:
            session.commit()
        except:
            session.rollback()
        finally:
            session.close()

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
    finally:
        session.close()


def user_login(event, context):

    """
    Logs in a user.
    :param event: Login JSON as a dict.
    :context: AWS context
    """

    # Creates session. No try-catch logic because nothing is inserted.
    session = Session(engine)
    try:

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
    except:
        session.rollback()
        raise
    finally:
        session.close()
