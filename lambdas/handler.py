import json
import urllib.parse
import base64
import secrets
import hashlib
import os
import traceback
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import advito.util
from advito.service.user import UserService, serialize_user, deserialize_user, deserialize_user_create
from advito.service.application_role import ApplicationRoleService, serialize_application_role
from advito.service.amorphous import AmorphousService
from advito.service.client import ClientService, serialize_client, deserialize_client, deserialize_client_create#, serialize_client_division
from advito.error import AdvitoError, NotFoundError, LogoutError, LoginError, BadRequestError, InvalidSessionError, ExpiredSessionError, UnauthorizedError
from advito.role import Role


# Unpacks environment variables to build DB client and services
session_duration_sec = int(os.environ['SESSION_DURATION_SEC'])
db_connection = os.environ['DB_CONNECTION']
email_sender = os.environ['EMAIL_SENDER']
email_region_name = os.environ['EMAIL_REGION_NAME']
email_charset = os.environ['EMAIL_CHARSET']
email_client = boto3.client('ses', region_name=email_region_name)

# Creates SQLAlchemy DB client
engine = create_engine(db_connection)

# Creates services that control business logic
user_service = UserService(session_duration_sec)
application_role_service = ApplicationRoleService(user_service)
amorphous_service = AmorphousService()
client_service = ClientService()

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

        except (NotFoundError, LoginError, LogoutError) as e:
            session.rollback()
            body = {
                "success": False,
                "apicode": "NOT FOUND",
                "apimessage": str(e),
                "apidataset": None
            }
            status_code = 400

        except (InvalidSessionError, UnauthorizedError) as e:
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
                "apimessage": "Database rejected update/insert",
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
                "apimessage": "Unexpected exception occurred",
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


def authenticate_decorator(roles=[]):

    """
    Generates a decorator function that, when used, checks that the token in the request exists in the database and is not expired.
    Then, checks that the session token is that of an admin user.
    After the checks, it invokes the underlying function.
    """
    def wrapper_generator(func):

        def wrapper(event, context, session):

            # Validates that user is logged in
            session_token = event.get('sessionToken')
            if session_token is None:
                raise InvalidSessionError('Required field "sessionToken" not supplied.')

            # Ensures that user is logged in has correct role
            user_service.validate_logged_in(session_token, session, roles)

            # Invokes underlying function
            return func(event, context, session)

        return wrapper

    # Returns decorated function
    return wrapper_generator



###################### Handlers ###########################


def test_email(event, context):

    """
    Tests sending an email
    """

    try:
        response = email_client.send_email(
            Destination = {
                "ToAddresses": [ "Jhuebner@guruconsult.com" ],
            },
            Message = {
                "Body": {
                    "Text": {
                        "Charset": email_charset,
                        "Data": "Congratulations! You have been randomly selected to receive this email! You just wasted 10 seconds of your life!"
                    }
                },
                "Subject": {
                    "Charset": email_charset,
                    "Data": "Congratulations!"
                }
            },
            Source = email_sender
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:")
        print(response['MessageId'])





@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def user_create(event, context, session):

    """
    Reads a user from the event body and inserts it into the database.
    :param event: User JSON as a dict.
    :param context: AWS context.
    :param session: Session used for database connectivity.
    """

    # Deserializes user from event

    user = deserialize_user_create(event)

    # Acquires role from event
    roleId = event['roleId']
    role = Role(roleId)

    # Creates user and assigns it a role
    user_service.create(user, session)
    session.flush()
    application_role_service.create_for(user.id, role, session)

    # Creates response and returns it
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully created",
        "apidataset": "User successfully created"
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
    username = event['username']
    password = event['pwd']

    # Tries to login
    (user, user_session) = user_service.login(username, password, session)
    session.commit()

    # Creates response and returns it
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully logged in",
        "apidataset": {
            "displayName": user.name_first + " " + user.name_last,
            "clientId": user.client_id,
            "profilePicturePath": user.profile_picture_path,
            "sessionToken": user_session.session_token
        }
    }


@handler_decorator
@authenticate_decorator()
def user_get(event, context, session):

    """
    Acquires a user by their session token.
    :param event: Token JSON as dict. Example:
    {
        "sessionToken": "abc123"
    }
    :param context: AWS context.
    :param session: Session used for database connectivity.
    """

    # Acquires session token
    session_token = event['sessionToken']
    user = user_service.get(session_token, session)
    user_json = serialize_user(user)

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully fetched",
        "apidataset": user_json
    }


@handler_decorator
@authenticate_decorator()
def user_logout(event, context, session):

    """
    Logs out a user.
    :param event: Logout JSON as a dict. Example:
    {
        "sessionToken": "abc123"
    }
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
        "apimessage": "User successfully logged out",
        "apidataset": "User successfully logged out"
    }


@handler_decorator
@authenticate_decorator()
def user_update(event, context, session):

    """
    Updates an existing users data.
    :param event: User Update JSON as a dict.
    """

    # Deserializes user from event
    session_token = event['sessionToken']
    user = deserialize_user(event)
    current_user = user_service.get(session_token, session)
    user.id = current_user.id

    # Creates user and assigns it a role
    user_service.update(user, session)

    # Creates response and returns it
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully updated",
        "apidataset": "User successfully updated"
    }

@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def user_update_any(event, context, session):

    """
    Updates an existing users data.
    Unlike user_update, any user an be updated.
    This endpoint requires admin privileges.
    :param event: User Update JSON as a dict.
    """

    # Deserializes user from event
    session_token = event['sessionToken']
    roleId = event['roleId']
    role = Role(roleId)
    user = deserialize_user(event)
    user.id = event["userId"]
    if user.id is None:
        raise BadRequestError("id must be specified.")

    # Creates user and assigns it a role
    user_service.update_any(user, session)
    application_role_service.update_for(user.id, role, session)

    # Creates response and returns it
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully updated",
        "apidataset": "User successfully updated"
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def user_access(event, context, session):

    """
    Gets user access information for a given client.
    :param event: Login JSON as a dict. Example:
    {
        "sessionToken": "abc123",
        "clientId": 1
    }
    :param context: AWS context.
    :param session: Session used for database connectivity.
    """

    # Gets users that belong to specified client
    client_id = event['clientId']
    results = application_role_service.get_user_access_by_client(client_id, session)

    # Serializes each user/role pair as json objects
    serialized = []
    for result in results:
        user = result[0]
        role = result[1]
        entry = {
            "userId": user.id,
            "nameFirst": user.name_first,
            "nameLast": user.name_last,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "address": user.address,
            "isEnabled": user.is_enabled,
            "role": role.role_name,
            "roleId": role.id
        }
        serialized.append(entry)

    # Returns response
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": serialized
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_get_all(event, context, session):

    """
    Gets information about a client given a user's session tokenself.
    Only administrators may invoke this endpoint.
    """

    # Gets clients and deserializes them as json
    clients = client_service.get_all(session)
    clients = [serialize_client(client) for client in clients]

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Clients successfully fetched",
        "apidataset": clients
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_update(event, context, session):

    """
    Updates a clients info.
    Only administrators may invoke this endpoint.
    """

    client = deserialize_client(event)
    client_service.update(client, session)

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Client successfully updated",
        "apidataset": "Client successfully updated"
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_create(event, context, session):

    """
    Creates a new client
    Only administrators may invoke this endpoint.
    """

    client = deserialize_client_create(event)
    client_service.create(client, session)
    session.flush()
    new_client_serialized = serialize_client(client)

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Client successfully created",
        "apidataset": new_client_serialized
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_division_get_all(event, context, session):

    """
    Gets client divisions of a given client
    """

    client_id = event['clientId']
    client_division = client_service.get_divisions(client_id, session)
    serialized_division = serialize_client_division(client_division)

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Client successfully created",
        "apidataset": serialized_division
    }





@handler_decorator
@authenticate_decorator()
def udf_story_air(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_air(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_air_airlines(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_air_airlines(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_air_cabins(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_air_cabins(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_air_routes(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_air_routes(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }


@handler_decorator
@authenticate_decorator()
def udf_story_air_traffic(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_air_traffic(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_hotel(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel_1(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_hotel_1(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel_2(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_hotel_2(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel_3(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_hotel_3(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel_4(event, context, session):
    client_id = event['clientId']
    result = amorphous_service.udf_story_hotel_4(client_id, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }
