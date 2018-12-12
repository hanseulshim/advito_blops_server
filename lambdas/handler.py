from sqlalchemy import create_engine
from service.user import Users
import json
import hashlib
import secrets
import base64
import os

# Creates db client
db_conn_string = os.environ['DB_CONNECTION']
db = create_engine(db_conn_string)

# Creates services
user_service = Users(db)


def create_user(event, context):
    user_in = event
    user_out = user_service.create(user_in)
    return {
        "statusCode": 200,
        "body": user_out
    }



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
