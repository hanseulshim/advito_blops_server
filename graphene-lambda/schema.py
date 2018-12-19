import graphene
import json
import boto3
import base64

lambda_client = boto3.client('lambda')

class ApiDataSet(graphene.ObjectType):
    displayName = graphene.String()
    sessionToken = graphene.String()

class ResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = ApiDataSet()

class LoginResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = ResponseBody()

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
        dataset = response_payload['apidataset']
        #apidataset = ApiDataSet(dataset['displayName'], dataset['sessionToken'])
        #responsebody = ResponseBody(True, dataset['apicode'], dataset['apimessage'])
        #responsebody.apidataset = apidataset
        #loginresponse = LoginResponse(200)
        #loginresponse.body = responsebody
        return response
        #return dataset['sessionToken']
        #return loginresponse
    else:
        return "Invalide username/password"

class Query(graphene.ObjectType):
    #login = graphene.String(username=graphene.String(), password=graphene.String())
    login = graphene.types.json.JSONString(username=graphene.String(), password=graphene.String())
    #login = graphene.Field(LoginResponse, username=graphene.String(), password=graphene.String())

    def resolve_login(self, info, username, password):
        return user_login(username, password)

schema = graphene.Schema(query=Query)

#ads = ApiDataSet('Hello', 'World')
#print(ads.displayName, ads.sessionToken)
#rb = ResponseBody(True, 'a', 'b')
#rb.apidataset = ads
#print(rb.success)




