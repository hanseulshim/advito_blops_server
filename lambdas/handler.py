import json
import requests
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
from advito.service.application import ApplicationService, serialize_application_with_features, serialize_feature
from advito.service.amorphous import AmorphousService
from advito.service.client import ClientService, serialize_client, deserialize_client, deserialize_client_create, serialize_client_division, deserialize_client_division, deserialize_client_division_create
from advito.error import AdvitoError, NotFoundError, LogoutError, LoginError, BadRequestError, InvalidSessionError, ExpiredSessionError, UnauthorizedError, TokenExpirationError
from advito.role import Role


# Unpacks environment variables to build DB client and services
session_duration_sec = int(os.environ['SESSION_DURATION_SEC'])
reset_password_duration_hours = int(os.environ['RESET_PASSWORD_DURATION_HOURS'])
db_connection = os.environ['DB_CONNECTION']

# Sets up email
email_sender = os.environ['EMAIL_SENDER']
email_region_name = os.environ['EMAIL_REGION_NAME']
email_charset = os.environ['EMAIL_CHARSET']
email_client = boto3.client('ses', region_name=email_region_name)

# Creates SQLAlchemy DB client
engine = create_engine(db_connection)

# Creates services that control business logic
user_service = UserService(session_duration_sec, reset_password_duration_hours)
application_role_service = ApplicationRoleService(user_service)
application_service = ApplicationService()
amorphous_service = AmorphousService()
client_service = ClientService()

################# Helpers #################
def send_email(recipient, subject, message):
    response = email_client.send_email (
        Destination = {
            "ToAddresses": [ recipient ],
        },
        Message = {
            "Body": {
                "Text": {
                    "Charset": email_charset,
                    "Data": message
                }
            },
            "Subject": {
                "Charset": email_charset,
                "Data": subject
            }
        },
        Source = email_sender
    )
    return response


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

        except (NotFoundError, LoginError, LogoutError, TokenExpirationError) as e:
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

def test_send_email(event, context):
    print("Sending http request")
    response = requests.get('https://github.com/timeline.json')
    print(response.json())
    print("Sending email")
    send_email('wcahill@boostlabs.com', 'Chicken Dinner', 'This is a message')

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
    print('Before')
    (user, role_ids, user_session) = user_service.login(username, password, session)
    session.commit()
    print('After')

    # Creates response and returns it
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully logged in",
        "apidataset": {
            "displayName": user.name_first + " " + user.name_last,
            "clientId": user.client_id,
            "roleIds": role_ids,
            "profilePicturePath": user.profile_picture_path,
            "sessionToken": user_session.session_token,
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
def user_authenticate(event, context, session):

    """
    Receives a sessionToken and returns user info as well as their roles.
    """

    # Gets session token
    session_token = event['sessionToken']

    # Gets user with that token and their roles
    user_roles = user_service.get_authentication_info(session_token, session)
    user = user_roles[0]
    roles = user_roles[1]
    role_names = [role.role_name for role in roles]

    apidataset = {
        "id": user.id,
        "email": user.email,
        "nameFirst": user.name_first,
        "nameLast": user.name_first,
        "roles": role_names
    }

    # Result
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "User successfully fetched",
        "apidataset": apidataset
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
    user.id = event["id"]
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
    Gets user access information for the Advito client.
    :param event: Login JSON as a dict. Example:
    {
        "sessionToken": "abc123",
    }
    :param context: AWS context.
    :param session: Session used for database connectivity.
    """

    # Gets users that belong to specified client
    results = application_role_service.get_advito_user_access(session)

    # Serializes each user/role pair as json objects
    serialized = []
    for result in results:
        user = result[0]
        role = result[1]
        entry = {
            "id": user.id,
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
def user_reset_password_start(event, context, session):

    """
    Starts the process of resetting a users password
    """

    # Gets recipient email
    recipient = event["email"]

    # Generates access token for password reset
    access_token = user_service.reset_password_start(recipient, session)

    # Sends email
    url = "http://fakeurl.com/" + access_token
    emailMessage = "Please visit the following URL to reset your password: " + url
    response = send_email(recipient, emailMessage)

    # Returns response
    message = "Email with url " + url + " sent to email " + email
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": message,
        "apidataset": message
    }


@handler_decorator
def user_reset_password_end(event, context, session):

    """
    Finalizes password reset for a given user
    """

    # Acquires credentials and new password
    access_token = event['accessToken']
    new_password = event['pwd']

    # Resets password
    user_service.reset_password_end(access_token, new_password, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Password successfully updated",
        "apidataset": "Password successfully updated"
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_get_all(event, context, session):

    """
    Gets information about a client given a user's session tokenself.
    Only administrators may invoke this endpoint.
    """

    # Gets clients and deserializes them as json
    print('Before get all')
    clients = client_service.get_all(session)
    print('After get all')
    clients = [serialize_client(client) for client in clients]
    print('After deserialization')

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
        "apidataset": "Client successfully created"
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_division_create(event, context, session):

    """
    Updates a single ClientDivision in the database
    """
    client_division = deserialize_client_division_create(event)
    client_service.create_division(client_division, session)

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Division successfully created",
        "apidataset": "Division successfully created"
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_division_get_all(event, context, session):

    """
    Gets client divisions of a given client
    """

    client_id = event['clientId']
    client_divisions = client_service.get_divisions(client_id, session)
    divisions_serialized = [serialize_client_division(div) for div in client_divisions]

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Divisions succesfully fetched",
        "apidataset": divisions_serialized
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_division_update(event, context, session):

    """
    Updates a single ClientDivision in the database
    """
    client_division = deserialize_client_division(event)
    client_service.update_division(client_division, session)

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Division successfully updated",
        "apidataset": "Division successfully updated"
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def client_set_features(event, context, session):

    """
    Sets client feature features by ids
    """

    client_id = event["clientId"]
    feature_ids = event["featureIds"]
    client_service.set_features(client_id, feature_ids, session)

    # Done
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Features successfully set",
        "apidataset": "Features successfully set"
    }


@handler_decorator
@authenticate_decorator([Role.ADMINISTRATOR])
def application_get(event, context, session):

    """
    Gets all applications that a client belongs to.
    Determines this by getting all features of the user and getting the applications those features belong to.
    """

    client_id = event.get("clientId")
    if client_id is None:
        applications_with_features = application_service.get_all(session)
    else:
        applications_with_features = application_service.get_by_client(client_id, session)
    applications_with_features_serialized = [serialize_application_with_features(app) for app in applications_with_features]
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Applications successfully fetched",
        "apidataset": applications_with_features_serialized
    }


@handler_decorator
@authenticate_decorator()
def udf_story_air(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_air(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_air_airlines(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_air_airlines(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_air_cabins(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_air_cabins(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_air_routes(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_air_routes(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }


@handler_decorator
@authenticate_decorator()
def udf_story_air_traffic(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_air_traffic(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_hotel(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel_1(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_hotel_1(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel_2(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_hotel_2(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel_3(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_hotel_3(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }

@handler_decorator
@authenticate_decorator()
def udf_story_hotel_4(event, context, session):
    session_token = event['sessionToken']
    result = amorphous_service.udf_story_hotel_4(session_token, session)
    return {
        "success": True,
        "apicode": "OK",
        "apimessage": "Data successfully fetched",
        "apidataset": result
    }
