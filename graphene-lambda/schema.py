import graphene
import json
import boto3
import base64

lambda_client = boto3.client('lambda')

# I should not name a variable type. We may have a serious problem here.
# Objects used Air Summary and Traffic Lane.
class KpisObject(graphene.ObjectType):
    title = graphene.String()
    value = graphene.Int()
    delta = graphene.Int()
    percent = graphene.Float()
    change = graphene.String()
    type = graphene.String()
    icon = graphene.String()

class BarchartDataObject(graphene.ObjectType):
    category = graphene.String()
    value = graphene.Float()
    change = graphene.String()

class BarchartObject(graphene.ObjectType):
    title = graphene.String()
    type = graphene.String()
    data = graphene.List(BarchartDataObject)

class CoordsObject(graphene.ObjectType):
    latitude = graphene.Float()
    longitude = graphene.Float()

class LocationsObject(graphene.ObjectType):
    thickness = graphene.Float()
    height = graphene.Float()
    opacity = graphene.Float()
    coords = graphene.List(CoordsObject)
    origin = graphene.String()
    destination = graphene.String()

class AirData(graphene.ObjectType):
    title = graphene.String()
    summary = graphene.String()
    kpis = graphene.List(KpisObject)
    barchart = graphene.List(BarchartObject)
    locations = graphene.List(LocationsObject)

# Objects used for Top Airlines and Cabin Use.
class AirlineSubCategories(graphene.ObjectType):
    name = graphene.String()
    value = graphene.Int()
    delta = graphene.Int()
    percent = graphene.Float()
    color = graphene.String()

class AirlineCategories(graphene.ObjectType):
    title = graphene.String()
    icon = graphene.String()
    total = graphene.Int()
    subCategories = graphene.List(AirlineSubCategories)

class Airline(graphene.ObjectType):
    title = graphene.String()
    summary = graphene.String()
    barchart = graphene.List(BarchartObject)
    categories = graphene.List(AirlineCategories)

# Objects used for Airline tickets by route types.
class AirRouteListElement(graphene.ObjectType):
    category = graphene.String()
    value = graphene.Int()
    prop = graphene.String()
    nextProp = graphene.String()

class DonutData(graphene.ObjectType):
    category = graphene.String()
    value = graphene.Float()
    nextLevel = graphene.String()

class AirRouteSub(graphene.ObjectType):
    title = graphene.String()
    summary = graphene.String()
    label = graphene.String()
    context = graphene.String()
    total = graphene.Int()
    colors = graphene.List(graphene.String)
    donutData = graphene.List(DonutData)

class AirRoute(graphene.ObjectType):
    donutData = graphene.Field(AirRouteSub)
    #airRoot = graphene.Field(AirRouteSub)
    #transatlantic = graphene.Field(AirRouteSub)
    #unitedStates = graphene.Field(AirRouteSub)
    #jfk = graphene.Field(AirRouteSub)

# Objects used for Hotel Summary and Hotel Spend.
class HotelBarchartDataObject(graphene.ObjectType):
    category = graphene.String()
    value = graphene.Float()
    delta = graphene.Float()
    change = graphene.String()
    percent = graphene.Float()

class HotelBarchartObject(graphene.ObjectType):
    title = graphene.String()
    type = graphene.String()
    data = graphene.List(HotelBarchartDataObject)

class HotelLocationsObject(graphene.ObjectType):
    title = graphene.String()
    radius = graphene.Float()
    latitude = graphene.Float()
    longitude = graphene.Float()

class HotelData(graphene.ObjectType):
    title = graphene.String()
    summary = graphene.String()
    kpis = graphene.List(KpisObject)
    barchart = graphene.List(HotelBarchartObject)
    locations = graphene.List(HotelLocationsObject)

# Room nights
class RoomNights(graphene.ObjectType):
    hotelRoot = graphene.Field(AirRouteSub)
    europe = graphene.Field(AirRouteSub)
    unitedKingdom = graphene.Field(AirRouteSub)

# Objects used for Hotel Chains and Hotel Tiers
# Objects used for Top Airlines and Cabin Use.
class HotelChainSubCategories(graphene.ObjectType):
    name = graphene.String()
    value = graphene.Float()
    color = graphene.String()

class HotelChainCategories(graphene.ObjectType):
    title = graphene.String()
    type = graphene.String()
    icon = graphene.String()
    total = graphene.Float()
    subCategories = graphene.List(HotelChainSubCategories)

class HotelChain(graphene.ObjectType):
    title = graphene.String()
    summary = graphene.String()
    categories = graphene.List(HotelChainCategories)
    barchart = graphene.List(HotelBarchartObject)

# The three classes below are used for creating the login response
# A LoginResponse is what is returned by the GraphQL login function.
# A LoginResponse contains a ResponseBody which contains a ApiDataSet.
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

class AirDataResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(AirData)

class AirlineResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(Airline)

class AirRouteResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(AirRouteSub)

class HotelDataResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(HotelData)

class RoomNightsResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(RoomNights)

class HotelChainResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(HotelChain)

class LoginResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(ResponseBody)

class LogoutResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(ResponseBody)

class AirDataResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(AirDataResponseBody)

class AirlineResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(AirlineResponseBody)

class AirRouteResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(AirRouteResponseBody)

class HotelDataResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(HotelDataResponseBody)

class RoomNightsResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(RoomNightsResponseBody)

class HotelChainResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(HotelChainResponseBody)

# This class defines the arguments required for the create advito user mutation and houses the mutation function.
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

# Defines the AdvitoUser class so that we can create and return AdvitoUser objects.
class AdvitoUser(graphene.ObjectType):
    client_id = graphene.Int()
    username = graphene.String()
    pwd = graphene.String()
    name_last = graphene.String()
    name_first = graphene.String()
    email = graphene.String()

# This class defines the mutations. More mutations can be added here in the future.
class MyMutations(graphene.ObjectType):
    create_advito_user = CreateAdvitoUser.Field()

class DashboardData(graphene.ObjectType):
    title = graphene.String()
    value = graphene.String()
    unit = graphene.String()
    programShare = graphene.Int()
    color = graphene.String()
    header = graphene.String()
    secondaryHeader = graphene.String()
    icon = graphene.String()
    alert = graphene.Boolean()

class Opportunities(graphene.ObjectType):
    prevCursor = graphene.Int()
    cursor = graphene.Int()
    totalOpportunities = graphene.Int()
    hasNext = graphene.Boolean()
    opportunities = graphene.List(DashboardData)

class RiskAreas(graphene.ObjectType):
    prevCursor = graphene.Int()
    cursor = graphene.Int()
    totalOpportunities = graphene.Int()
    hasNext = graphene.Boolean()
    riskAreas = graphene.List(DashboardData)

class SidebarData(graphene.ObjectType):
    header = graphene.String()
    secondaryHeader = graphene.String()
    icon = graphene.String()
    alert = graphene.Boolean()

class VDListObject(graphene.ObjectType):
    title = graphene.String()
    icon = graphene.String()
    domo = graphene.Boolean()
    link = graphene.String()

class ViewData(graphene.ObjectType):
    title = graphene.String()
    description = graphene.String()
    icon = graphene.String()
    disabled = graphene.Boolean()
    button = graphene.String()
    list = graphene.List(VDListObject)

# Response Body and Response class for noChangeSince
class NoChangeSinceResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.String()

class NoChangeSinceResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(NoChangeSinceResponseBody)

class DashboardDataResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.List(DashboardData)

class DashboardDataResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(DashboardDataResponseBody)

class ViewDataResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.List(ViewData)

class ViewDataResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(ViewDataResponseBody)

class OpportunitiesResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(Opportunities)

class OpportunitiesResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(OpportunitiesResponseBody)

class RiskAreasResponseBody(graphene.ObjectType):
    success = graphene.Boolean()
    apicode = graphene.String()
    apimessage = graphene.String()
    apidataset = graphene.Field(RiskAreas)

class RiskAreasResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(RiskAreasResponseBody)

# This is the function that the mutation function calls that actually invokes the lambda function for creating the user.
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

# This is the function called by the login resolver that passes the username and password to the login lambda function.
# It then receives the response from the login lambda and converts the response into an object that can be returned by graphQL.
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

def user_logout(sessionToken):
    payload = {"sessionToken": sessionToken}
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = 'python-lambdas-dev-user_logout',
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    response_payload = json.loads(response_dict["body"])
    responsebody = ResponseBody(response_payload['success'], response_payload['apicode'], response_payload['apimessage'])
    logoutresponse = LogoutResponse(response_dict['statusCode'])
    logoutresponse.body = responsebody

    return logoutresponse

def get_air_data_json(air_data):
    kpis_list = [KpisObject(k['title'], k['value'], k['delta'], k['percent'], k['change'], 
        k['type'], k['icon']) for k in air_data['kpis']]

    barchart_list = []
    for i in air_data['barchart']:
        bc_data_list = []
        for j in i['data']:
            bc_data_list += [BarchartDataObject(j['category'], j['value'], j['change'])]
        barchart_list += [BarchartObject(i['title'], i['type'], bc_data_list)]

    locations_list = []
    for i in air_data['locations']:
        coords_list = []
        for j in i['coords']:
            coords_list += [CoordsObject(j['latitude'], j['longitude'])]
        locations_list += [LocationsObject(i['thickness'], i['height'], i['opacity'], coords_list, i['origin'], i['destination'])]

    return AirData(air_data['title'], air_data['summary'], kpis_list, barchart_list, locations_list)

def get_air_data(clientId, sessionToken, functionName, story_name):
    payload = {"clientId": clientId, "sessionToken": sessionToken}
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = functionName,
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    response_payload = json.loads(response_dict["body"])
    responsebody = AirDataResponseBody(response_payload['success'], response_payload['apicode'], response_payload['apimessage'])
    airDataResponse = AirDataResponse(response_dict['statusCode'])

    if (response_dict['statusCode'] == 200):
        air_data = response_payload['apidataset']
        air_data = air_data[story_name]
        air_data_object = get_air_data_json(air_data)
        responsebody.apidataset = air_data_object

    airDataResponse.body = responsebody

    return airDataResponse

def get_airline_data_json(airline_data):
    barchart_list = []
    if 'barchart' in airline_data.keys():
        for i in airline_data['barchart']:
            bc_data_list = []
            for j in i['data']:
                bc_data_list += [BarchartDataObject(j['category'], j['value'], j['change'])]
            barchart_list += [BarchartObject(i['title'], i['type'], bc_data_list)]

    categories_list = []
    for i in airline_data['categories']:
        sub_categories_list = []
        for j in i['subcategories']:
            sub_categories_list += [AirlineSubCategories(j['name'], j['value'], j['delta'], j['percent'], j['color'])]
        categories_list += [AirlineCategories(i['title'], i['icon'], i['total'], sub_categories_list)]

    return Airline(airline_data['title'], airline_data['summary'], barchart_list, categories_list)

def get_airline_data(clientId, sessionToken, functionName, story_name):
    payload = {"clientId": clientId, "sessionToken": sessionToken}
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = functionName,
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    response_payload = json.loads(response_dict["body"])
    responsebody = AirlineResponseBody(response_payload['success'], response_payload['apicode'], response_payload['apimessage'])
    airlineResponse = AirlineResponse(response_dict['statusCode'])

    if (response_dict['statusCode'] == 200):
        airline_data = response_payload['apidataset']
        airline_data = airline_data[story_name]
        airline_data_object = get_airline_data_json(airline_data)
        responsebody.apidataset = airline_data_object

    airlineResponse.body = responsebody

    return airlineResponse

def get_airroute_data_json(airroute_data, title):
    donutData = airroute_data[title]
    #transatlantic = airroute_data['transatlantic']
    #unitedStates = airroute_data['unitedStates']
    #jfk = airroute_data['jfk']
    #airroute_data_list = [airRoot, transatlantic, unitedStates, jfk]
    airroute_data_list = [donutData]
    airroute_sub_list = []

    for airrouteObject in airroute_data_list:
        colors_list = [color for color in airrouteObject['colors']]

        donut_data_list = []
        for d in airrouteObject['donutData']:
            if 'nextLevel' in d.keys():
                donut_data_list += [DonutData(d['category'], d['value'], d['nextLevel'])]
            else:
                donut_data_list += [DonutData(d['category'], d['value'], '')]
        
        airroute_sub_list += [AirRouteSub(airrouteObject['title'], airrouteObject['summary'], airrouteObject['label'], 
            airrouteObject['context'], airrouteObject['total'], colors_list, donut_data_list)]

    return airroute_sub_list[0]

def get_airroute_data(clientId, sessionToken, functionName, story_name, title):
    payload = {"clientId": clientId, "sessionToken": sessionToken}
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = functionName,
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    response_payload = json.loads(response_dict["body"])
    responsebody = AirRouteResponseBody(response_payload['success'], response_payload['apicode'], response_payload['apimessage'])
    airrouteResponse = AirRouteResponse(response_dict['statusCode'])

    if (response_dict['statusCode'] == 200):
        airroute_data = response_payload['apidataset']
        airroute_data = airroute_data[story_name]
        airroute_data_object = get_airroute_data_json(airroute_data, title)
        responsebody.apidataset = airroute_data_object

    airrouteResponse.body = responsebody

    return airrouteResponse

def get_hotel_data_json(hotel_data):
    kpis_list = [KpisObject(k['title'], k['value'], k['delta'], k['percent'], k['change'],
        k['type'], k['icon']) for k in hotel_data['kpis']]

    barchart_list = []
    for i in hotel_data['barchart']:
        bc_data_list = []
        for j in i['data']:
            bc_data_list += [HotelBarchartDataObject(j['category'], j['value'], j['delta'], j['change'], j['percent'])]
        barchart_list += [HotelBarchartObject(i['title'], i['type'], bc_data_list)]

    locations_list = []
    if 'locations' in hotel_data.keys():
        locations_list = [HotelLocationsObject(l['title'], l['radius'], l['latitude'], l['longitude']) for l in hotel_data['locations']]

    return AirData(hotel_data['title'], hotel_data['summary'], kpis_list, barchart_list, locations_list)

def get_hotel_data(clientId, sessionToken, functionName, story_name):
    payload = {"clientId": clientId, "sessionToken": sessionToken}
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = functionName,
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    response_payload = json.loads(response_dict["body"])
    responsebody = HotelDataResponseBody(response_payload['success'], response_payload['apicode'], response_payload['apimessage'])
    hotelDataResponse = HotelDataResponse(response_dict['statusCode'])

    if (response_dict['statusCode'] == 200):
        hotel_data = response_payload['apidataset']
        hotel_data = hotel_data[story_name]
        hotel_data_object = get_hotel_data_json(hotel_data)
        responsebody.apidataset = hotel_data_object

    hotelDataResponse.body = responsebody

    return hotelDataResponse

def get_roomnight_data_json(roomnight_data):
    hotelRoot = roomnight_data['hotelRoot']
    europe = roomnight_data['europe']
    unitedKingdom = roomnight_data['unitedKingdom']
    roomnight_data_list = [hotelRoot, europe, unitedKingdom]
    roomnight_sub_list = []

    for roomnightObject in roomnight_data_list:
        colors_list = [color for color in roomnightObject['colors']]

        donut_data_list = []
        for d in roomnightObject['donutData']:
            if 'nextLevel' in d.keys():
                donut_data_list += [DonutData(d['category'], d['value'], d['nextLevel'])]
            else:
                donut_data_list += [DonutData(d['category'], d['value'], '')]
        
        roomnight_sub_list += [AirRouteSub(roomnightObject['title'], roomnightObject['summary'], roomnightObject['label'], 
            roomnightObject['context'], roomnightObject['total'], colors_list, donut_data_list)]

    return RoomNights(roomnight_sub_list[0], roomnight_sub_list[1], roomnight_sub_list[2])

def get_roomnight_data(clientId, sessionToken, functionName, story_name):
    payload = {"clientId": clientId, "sessionToken": sessionToken}
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = functionName,
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    response_payload = json.loads(response_dict["body"])
    responsebody = RoomNightsResponseBody(response_payload['success'], response_payload['apicode'], response_payload['apimessage'])
    roomnightResponse = RoomNightsResponse(response_dict['statusCode'])

    if (response_dict['statusCode'] == 200):
        roomnight_data = response_payload['apidataset']
        roomnight_data = roomnight_data[story_name]
        roomnight_data_object = get_roomnight_data_json(roomnight_data)
        responsebody.apidataset = roomnight_data_object

    roomnightResponse.body = responsebody

    return roomnightResponse

def get_hotelchain_data_json(hotelchain_data):
    barchart_list = []
    if 'barchart' in hotelchain_data.keys():
        for i in hotelchain_data['barchart']:
            bc_data_list = []
            for j in i['data']:
                if 'value' in j.keys():
                    bc_data_list += [HotelBarchartDataObject(j['category'], j['value'], j['delta'], j['change'], j['percent'])]
                else:
                    bc_data_list += [HotelBarchartDataObject(j['category'], 0, j['delta'], j['change'], j['percent'])]
            barchart_list += [HotelBarchartObject(i['title'], i['type'], bc_data_list)]

    categories_list = []
    for i in hotelchain_data['categories']:
        sub_categories_list = []
        for j in i['subCategories']:
            if 'value' in j.keys():
                sub_categories_list += [HotelChainSubCategories(j['name'], j['value'], j['color'])]
            else:
                sub_categories_list += [HotelChainSubCategories(j['name'], 0, j['color'])]
        if ('type' in i.keys()):
            categories_list += [HotelChainCategories(i['title'], i['type'], i['icon'], i['total'], sub_categories_list)]
        else:
            categories_list += [HotelChainCategories(i['title'], '', i['icon'], i['total'], sub_categories_list)]

    return HotelChain(hotelchain_data['title'], hotelchain_data['summary'], categories_list, barchart_list)

def get_hotelchain_data(clientId, sessionToken, functionName, story_name):
    payload = {"clientId": clientId, "sessionToken": sessionToken}
    payload_str = json.dumps(payload)
    encoded_str = payload_str.encode('ascii')

    invoke_response = lambda_client.invoke(
        FunctionName = functionName,
        InvocationType = 'RequestResponse',
        ClientContext = base64.b64encode(encoded_str).decode('utf-8'),
        Payload=bytes(encoded_str)
    )

    response = invoke_response['Payload'].read().decode('utf-8')
    response_dict = json.loads(response)
    response_payload = json.loads(response_dict["body"])
    responsebody = HotelChainResponseBody(response_payload['success'], response_payload['apicode'], response_payload['apimessage'])
    hotelchainResponse = HotelChainResponse(response_dict['statusCode'])

    if (response_dict['statusCode'] == 200):
        hotelchain_data = response_payload['apidataset']
        hotelchain_data = hotelchain_data[story_name]
        hotelchain_data_object = get_hotelchain_data_json(hotelchain_data)
        responsebody.apidataset = hotelchain_data_object

    hotelchainResponse.body = responsebody

    return hotelchainResponse

def get_noChangeSince(clientId, sessionToken):
    if (len(sessionToken) != 0):
        noChangeSinceResponse = NoChangeSinceResponse(200)
        noChangeSinceResponseBody = NoChangeSinceResponseBody(True, "OK", "Data successfully fetched.", "July 30")
    else:
        noChangeSinceResponse = NoChangeSinceResponse(400)
        noChangeSinceResponseBody = NoChangeSinceResponseBody(False, "INVALID", "No session found", "")
    noChangeSinceResponse.body = noChangeSinceResponseBody

    return noChangeSinceResponse

def get_DashBoardData_List(clientId, sessionToken, queryName):
    dashboardDataList = []
    dashboardDataResponse = DashboardDataResponse(200)
    dashboardDataResponseBody = DashboardDataResponseBody(True, "OK", "Data successfully fetched.")

    if (queryName == 'program_performance'):
        dashboardDataList = [
            DashboardData(title = 'Average Total Trip Cost', value = '$2,754', unit = ''),
            DashboardData(title = 'Booking Outside of Agency', value = '12% / $360K', unit = 'impact'),
            DashboardData(title = 'Expenses Out of Policy', value = '23% / $690K', unit = 'impact')
        ]
    elif (queryName == 'persona_list'):
        dashboardDataList = [
            DashboardData(title = 'road warrior', value = '$3,350', programShare = 25, color = '#ACD2CF'),
            DashboardData(title = 'executive', value = '$3,150', programShare = 40, color = '#90C3C1'),
            DashboardData(title = 'deal maker', value = '$2,561', programShare = 15, color = '#81BDB9'),
            DashboardData(title = 'on demand', value = '$1,955', programShare = 10, color = '#71B5B1')
        ]
    elif (queryName == 'activeAlerts'):
        dashboardDataList = [
            DashboardData(header = '', secondaryHeader = 'Leakage to Program is 3.5', 
                icon = 'air.png', alert = True),
            DashboardData(header = '', secondaryHeader = 'Performance against target is 6.5', 
                icon = 'air.png', alert = True),
            DashboardData(header = '', secondaryHeader = 'Performance against target is 6.1', 
                icon = 'air.png', alert = True),
            DashboardData(header = '', secondaryHeader = 'ATP to ancillary spend is 5.2', 
                icon = 'air.png', alert = True)
        ]
    elif (queryName == 'upcomingActions'):
        dashboardDataList = [
            DashboardData(header = 'October 31, 2018', secondaryHeader = '2nd Round Hotel Negotiations Due', 
                icon = 'flag.png', alert = False),
            DashboardData(header = 'January 31, 2018', secondaryHeader = 'Hotel Audits Due', 
                icon = 'flag.png', alert = False),
            DashboardData(header = 'Febuary 11, 2019', secondaryHeader = 'Delta Contract Expires', 
                icon = 'flag.png', alert = False)
        ]
    
    dashboardDataResponseBody.apidataset = dashboardDataList
    dashboardDataResponse.body = dashboardDataResponseBody

    return dashboardDataResponse

def get_ViewData_List(clientId, sessionToken, queryName):
    viewDataList = []
    viewDataResponse = ViewDataResponse(200)
    viewDataResponseBody = ViewDataResponseBody(True, "OK", "Data successfully fetched.")

    if (queryName == 'viewData'):
        list1 = [
            VDListObject(title = 'Travel Manager Dashboard', icon = 'manager_active.png', link = '/travel'),
            VDListObject(title = 'Executive Dashboard', icon = 'manager_active.png', link = '/executive'),
            VDListObject(title = 'Card Deck', icon = 'domo_active.png', domo = True, link = 'https://www.domo.com/')
        ]
        list2 = [
            VDListObject(title = 'Air program analytics', icon = 'manager_disabled.png', link = '#'),
            VDListObject(title = 'Air program manager (A3)', icon = 'tool_disabled.png', link = '#')
        ]
        list3 = [
            VDListObject(title = 'Hotel program analytics', icon = 'manager_disabled.png', link = '#'),
            VDListObject(title = 'Hotel program manager (HPM)', icon = 'tool_disabled.png', link = '#')
        ]
        viewDataList = [
            ViewData(title = '360 analytics', icon = '360_console.png', disabled = False, list = list1),
            ViewData(title = 'air', icon = 'air_console.png', disabled = True, list = list2),
            ViewData(title = 'hotel', icon = 'hotel_console.png', disabled = True, list = list3)
        ]
    if (queryName == 'infoData'):
        viewDataList = [
            ViewData(title = 'Webinar Name', description = 'Information about webinar', 
                icon = 'webinar_disabled.png', disabled = True, button = 'register'),
            ViewData(title = 'Document Library', description = 'Information about library',
                icon = 'library_active.png', disabled = False),
            ViewData(title = 'Podcast', description = 'Information about podcast',
                icon = 'podcast_disabled.png', disabled = True, button = 'download'),
            ViewData(title = 'Item Name', description = 'Information about item',
                icon = 'item_disabled.png', disabled = True, button = 'download')
        ]

    viewDataResponseBody.apidataset = viewDataList
    viewDataResponse.body = viewDataResponseBody

    return viewDataResponse

def get_Opportunities(clientId, sessionToken, limit, cursor, queryName):
    opportunitiesResponse = OpportunitiesResponse(200)
    opportunitiesResponseBody = OpportunitiesResponseBody(True, "OK", "Data successfully fetched.")

    if (queryName == 'opportunities'):
        opportunities_list = [
            DashboardData(title = 'Expenses approved above rate caps / per diems', value = '27% /$375K', unit = 'impact'),
            DashboardData(title = 'ABR higher than ANR', value = '30% / $500K', unit = 'impact'),
            DashboardData(title = 'NRT Utilization/Loss', value = '83% / $23K', unit = 'expired'),
            DashboardData(title = 'ANR higher than ABR', value = '25% / $100K', unit = 'expired'),
            DashboardData(title = 'New item', value = 'XX% / $XX', unit = 'impact'),
            DashboardData(title = 'New item', value = 'XX% / $XX', unit = 'expired'),
            DashboardData(title = 'New item', value = 'XX% / $XX', unit = ''),
        ]

        if (limit == None):
            limit = len(opportunities_list)

        totalOpportunities = len(opportunities_list)
        newCursor = cursor + limit
        prevCursor = 0
        hasNext = newCursor < totalOpportunities

        if (cursor - limit >= 0):
            prevCursor = cursor - limit

        opportunitiesResponseBody.apidataset = Opportunities(prevCursor, newCursor, totalOpportunities, hasNext, opportunities_list[cursor:newCursor])

    opportunitiesResponse.body = opportunitiesResponseBody

    return opportunitiesResponse

def get_RiskAreas(clientId, sessionToken, limit, cursor, queryName):
    riskAreasResponse = RiskAreasResponse(200)
    riskAreasResponseBody = RiskAreasResponseBody(True, "OK", "Data successfully fetched.")

    if (queryName == 'riskAreas'):
        risk_areas_list = [
            DashboardData(title = 'Number of markets with ATP change more than 15%', value = '10'),
            DashboardData(title = 'Number of markets with rate availability lower than 80%', value = '14'),
            DashboardData(title = 'Travelers in HRC/Markets', value = '512'),
            DashboardData(title = 'Hosts in TBS/Markets', value = '125'),
            DashboardData(title = 'New item', value = 'XXX'),
            DashboardData(title = 'New item', value = 'XXX'),
            DashboardData(title = 'New item', value = 'XXX')
        ]

        if (limit == None):
            limit = len(risk_areas_list)

        totalOpportunities = len(risk_areas_list)
        newCursor = cursor + limit
        prevCursor = 0
        hasNext = newCursor < totalOpportunities

        if (cursor - limit >= 0):
            prevCursor = cursor - limit

        riskAreasResponseBody.apidataset = RiskAreas(prevCursor, newCursor, totalOpportunities, hasNext, risk_areas_list[cursor:newCursor])

    riskAreasResponse.body = riskAreasResponseBody

    return riskAreasResponse

class Query(graphene.ObjectType):
    login = graphene.Field(LoginResponse, username=graphene.String(), password=graphene.String())
    logout = graphene.Field(LogoutResponse, sessionToken=graphene.String())
    
    airSummary = graphene.Field(AirDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    airTraffic = graphene.Field(AirDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    airAirlines = graphene.Field(AirlineResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    airCabins = graphene.Field(AirlineResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    donut = graphene.Field(AirRouteResponse, clientId=graphene.Int(), sessionToken=graphene.String(), title=graphene.String())

    hotelSummary = graphene.Field(HotelDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    roomNights = graphene.Field(RoomNightsResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    hotelSpend = graphene.Field(HotelDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    topHotelChains = graphene.Field(HotelChainResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    topHotelTiers = graphene.Field(HotelChainResponse, clientId=graphene.Int(), sessionToken=graphene.String(), title=graphene.String())

    advitoUser = graphene.Field(AdvitoUser)
    
    #programPerformance = graphene.List(DashboardData)
    programPerformance = graphene.Field(DashboardDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    noChangeSince = graphene.Field(NoChangeSinceResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    personaList = graphene.Field(DashboardDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    opportunities = graphene.Field(OpportunitiesResponse, clientId=graphene.Int(), sessionToken=graphene.String(), 
        limit=graphene.Int(), cursor=graphene.Int())
    riskAreas = graphene.Field(RiskAreasResponse, clientId=graphene.Int(), sessionToken=graphene.String(),
        limit=graphene.Int(), cursor=graphene.Int())
    upcomingActions = graphene.Field(DashboardDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    activeAlerts = graphene.Field(DashboardDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    viewData = graphene.Field(ViewDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    infoData = graphene.Field(ViewDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    
    def resolve_login(self, info, username, password):
        return user_login(username, password)  

    def resolve_logout(self, info, sessionToken):
        return user_logout(sessionToken)

    def resolve_airSummary(self, info, clientId, sessionToken):
        return get_air_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_air', 'udf_story_air')

    def resolve_airTraffic(self, info, clientId, sessionToken):
        return get_air_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_air_traffic', 'udf_story_air_traffic')

    def resolve_airAirlines(self, info, clientId, sessionToken):
        return get_airline_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_air_airlines', 'udf_story_air_airlines')

    def resolve_airCabins(self, info, clientId, sessionToken):
        return get_airline_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_air_cabins', 'udf_story_air_cabins')

    def resolve_donut(self, info, clientId, sessionToken, title):
        if (title in ['airRoot', 'transatlantic', 'unitedStates', 'jfk']):
            return get_airroute_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_air_routes', 'udf_story_air_routes', title)
        elif (title in ['hotelRoot', 'europe', 'unitedKingdom']):
            return get_airroute_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_hotel_4', 'udf_story_hotel_4', title)

    def resolve_hotelSummary(self, info, clientId, sessionToken):
        return get_hotel_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_hotel', 'udf_story_hotel')
    
    def resolve_roomNights(self, info, clientId, sessionToken):
        return get_roomnight_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_hotel_4', 'udf_story_hotel_4')

    def resolve_hotelSpend(self, info, clientId, sessionToken):
        return get_hotel_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_hotel_1', 'udf_story_hotel_1')

    def resolve_topHotelChains(self, info, clientId, sessionToken):
        return get_hotelchain_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_hotel_2', 'udf_story_hotel_2')

    def resolve_topHotelTiers(self, info, clientId, sessionToken):
        return get_hotelchain_data(clientId, sessionToken, 'python-lambdas-dev-udf_story_hotel_3', 'udf_story_hotel_3')

    def resolve_programPerformance(self, info, clientId, sessionToken):
        return get_DashBoardData_List(clientId, sessionToken, 'program_performance')

    def resolve_noChangeSince(self, info, clientId, sessionToken):
        return get_noChangeSince(clientId, sessionToken)

    def resolve_personaList(self, info, clientId, sessionToken):
        return get_DashBoardData_List(clientId, sessionToken, 'persona_list')

    def resolve_opportunities(self, info, clientId, sessionToken, limit = None, cursor = 0):
        return get_Opportunities(clientId, sessionToken, limit, cursor, 'opportunities')

    def resolve_riskAreas(self, info, clientId, sessionToken, limit = None, cursor = 0):
        return get_RiskAreas(clientId, sessionToken, limit, cursor, 'riskAreas')

    def resolve_upcomingActions(self, info, clientId, sessionToken):
        return get_DashBoardData_List(clientId, sessionToken, 'upcomingActions')

    def resolve_activeAlerts(self, info, clientId, sessionToken):
        return get_DashBoardData_List(clientId, sessionToken, 'activeAlerts')

    def resolve_viewData(self, info, clientId, sessionToken):
        return get_ViewData_List(clientId, sessionToken, 'viewData')

    def resolve_infoData(self, info, clientId, sessionToken):
        return get_ViewData_List(clientId, sessionToken, 'infoData')

schema = graphene.Schema(query=Query, mutation=MyMutations)

def test_fun():
    with open('data/air_summary.json') as f:
        as_data = json.load(f)

    return as_data




