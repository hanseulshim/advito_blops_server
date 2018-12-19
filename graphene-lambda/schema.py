import graphene
import json
import boto3
import base64

lambda_client = boto3.client('lambda')

def dummy_login(username, password):
    return True

def user_login(username, password):
    payload_str = '{"username": "' + username + '", "pwd": "' + password + '"}'
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = 'python-lambdas-dev-user_login',
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    
    if (response_dict["statusCode"] == 200):
        response_payload = json.loads(response_dict["body"])
        session_token = response_payload['apidataset']['sessionToken']
        return session_token
    else:
        return "Invalide username/password"

class Query(graphene.ObjectType):
    login = graphene.String(username=graphene.String(), password=graphene.String())

    def resolve_login(self, info, username, password):
        return user_login(username, password)

schema = graphene.Schema(query=Query)


