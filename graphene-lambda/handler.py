import json
import graphene
from schema import schema

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    print('Things')
    return response

def create_response(event, context, schema):
    pass

def graphqlHandler(event, context):
    try:
        return create_response(event, context, schema=schema)
    except Exception as e:
        print(e)
        raise e
    return response

if __name__ == "__main__":
    hello('','')

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
