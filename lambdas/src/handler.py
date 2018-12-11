from sqlalchemy import create_engine
from .service.user import Users
import json
import hashlib
import secrets
import base64
import os


def create_user(event, context):

    """
    Adds a user into the database
    When inserting the user, both base64(utf8(password + salt)) and base64(salt) are stored.
    """

    # Unpacks parameters
    username = event['username']
    password = event['password']
    email = event['email']

    # Salts password
    password_bytes = password.encode(encoding='UTF-8')
    salt_bytes = secrets.token_bytes(16)
    combined_bytes = password_bytes + salt_bytes

    # Converts both combined password and salt to base64-encoded strings
    combined = base64.b64encode(combined_bytes)
    salt = base64.b64encode(salt_bytes)

    # Stores user in db
    connection_str = os.environ['DB_CONNECTION']
    print(connection_str)


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
