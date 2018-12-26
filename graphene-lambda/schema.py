import graphene
import json
import boto3
import base64

lambda_client = boto3.client('lambda')

class ApiDataSet(graphene.ObjectType):
    displayName = graphene.String()
    clientId = graphene.Int()
    profilePicturePath = graphene.String()
    sessionToken = graphene.String()

class ResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(ApiDataSet)

class LoginResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(ResponseBody)

class CreateAdvitoUser(graphene.Mutation):
    class Arguments:
        client_id = graphene.Int()
        username = graphene.String()
        pwd = graphene.String()
        name_last = graphene.String()
        name_first = graphene.String()
        email = graphene.String()

    advitoUser = graphene.Field(lambda: AdvitoUser)

    def mutate(self, info, client_id, username, pwd, name_last, name_first, email):
        advitoUser = AdvitoUser(
          client_id=client_id,
          username=username,
          pwd=pwd,
          name_last=name_last,
          name_first=name_first,
          email=email
        )

        create_user(client_id, username, pwd, name_last, name_first, email)

        return CreateAdvitoUser(advitoUser=advitoUser)

class AdvitoUser(graphene.ObjectType):
    client_id = graphene.Int()
    username = graphene.String()
    pwd = graphene.String()
    name_last = graphene.String()
    name_first = graphene.String()
    email = graphene.String()


class MyMutations(graphene.ObjectType):
    create_advito_user = CreateAdvitoUser.Field()

def create_user(client_id, username, pwd, name_last, name_first, email):

    payload = {
        "clientId": client_id,
        "username": username,
        "pwd": pwd,
        "email": email,
        "phone": "123-4567",
        "profilePicturePath": "/",
        "timezoneDefault": "EST",
        "languageDefault": "English"
    }
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = 'python-lambdas-dev-user_create',
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

def user_login(username, pwd):

    payload = {
        "username": username,
        "pwd": pwd
    }
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = 'python-lambdas-dev-user_login',
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    response_payload = json.loads(response_dict["body"])
    responsebody = ResponseBody(response_payload['success'], response_payload['apicode'], response_payload['apimessage'])
    loginresponse = LoginResponse(response_dict['statusCode'])

    if (response_dict['statusCode'] == 200):
        dataset = response_payload['apidataset']
        apidataset = ApiDataSet(dataset['displayName'], dataset['clientId'], dataset['profilePicturePath'], dataset['sessionToken'])
        responsebody.apidataset = apidataset

    loginresponse.body = responsebody

    return loginresponse

class Query(graphene.ObjectType):
    login = graphene.Field(LoginResponse, username=graphene.String(), password=graphene.String())

    advitoUser = graphene.Field(AdvitoUser)

    def resolve_login(self, info, username, password):
        return user_login(username, password)

schema = graphene.Schema(query=Query, mutation=MyMutations)
