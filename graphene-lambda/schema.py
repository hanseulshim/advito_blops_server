import graphene
import json
import boto3
import base64

lambda_client = boto3.client('lambda')

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

class LoginResponse(graphene.ObjectType):
    statusCode = graphene.Int()
    body = graphene.Field(ResponseBody)

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

class Query(graphene.ObjectType):
    login = graphene.Field(LoginResponse, username=graphene.String(), password=graphene.String())
    advitoUser = graphene.Field(AdvitoUser)
    programPerformance = graphene.List(DashboardData)
    noChangeSince = graphene.String()
    personaList = graphene.List(DashboardData)
    opportunities = graphene.List(DashboardData)
    riskAreas = graphene.List(DashboardData)
    upcomingActions = graphene.List(SidebarData)
    activeAlerts = graphene.List(SidebarData)
    viewData = graphene.List(ViewData)
    infoData = graphene.List(ViewData)
    
    def resolve_login(self, info, username, password):
        return user_login(username, password)  

    def resolve_programPerformance(self, info):
        program_performance_list = [
            DashboardData(title = 'Average Total Trip Cost', value = '$2,754', unit = ''),
            DashboardData(title = 'Booking Outside of Agency', value = '12% / $360K', unit = 'impact'),
            DashboardData(title = 'Expenses Out of Policy', value = '23% / $690K', unit = 'impact')
        ]
        return program_performance_list

    def resolve_noChangeSince(self, info):
        return 'July 30'

    def resolve_personaList(self, info):
        persona_list = [
            DashboardData(title = 'road warrior', value = '$3,350', programShare = 25, color = '#ACD2CF'),
            DashboardData(title = 'executive', value = '$3,150', programShare = 40, color = '#90C3C1'),
            DashboardData(title = 'deal maker', value = '$2,561', programShare = 15, color = '#81BDB9'),
            DashboardData(title = 'on demand', value = '$1,955', programShare = 10, color = '#71B5B1')
        ]
        return persona_list

    def resolve_opportunities(self, info):
        opportunities_list = [
            DashboardData(title = 'Expenses approved above rate caps / per diems', value = '27% /$375K', unit = 'impact'),
            DashboardData(title = 'ABR higher than ANR', value = '30% / $500K', unit = 'impact'),
            DashboardData(title = 'NRT Utilization/Loss', value = '83% / $23K', unit = 'expired'),
            DashboardData(title = 'ANR higher than ABR', value = '25% / $100K', unit = 'expired'),
            DashboardData(title = 'New item', value = 'XX% / $XX', unit = 'impact'),
            DashboardData(title = 'New item', value = 'XX% / $XX', unit = 'expired'),
            DashboardData(title = 'New item', value = 'XX% / $XX', unit = ''),
        ]
        return opportunities_list

    def resolve_riskAreas(self, info):
        risk_areas_list = [
            DashboardData(title = 'Number of markets with ATP change more than 15%', value = '10'),
            DashboardData(title = 'Number of markets with rate availability lower than 80%', value = '14'),
            DashboardData(title = 'Travelers in HRC/Markets', value = '512'),
            DashboardData(title = 'Hosts in TBS/Markets', value = '125'),
            DashboardData(title = 'New item', value = 'XXX'),
            DashboardData(title = 'New item', value = 'XXX'),
            DashboardData(title = 'New item', value = 'XXX')
        ]
        return risk_areas_list

    def resolve_upcomingActions(self, info):
        upcoming_actions_list = [
            SidebarData('October 31, 2018', '2nd Round Hotel Negotiations Due', 'flag.png', False),
            SidebarData('January 31, 2018', 'Hotel Audits Due', 'flag.png', False),
            SidebarData('Febuary 11, 2019', 'Delta Contract Expires', 'contracts.png', False)
        ]
        return upcoming_actions_list

    def resolve_activeAlerts(self, info):
        active_alert_list = [
            SidebarData('', 'Leakage to Program is 3.5', 'air.png', True),
            SidebarData('', 'Performance against target is 6.5', 'air.png', True),
            SidebarData('', 'Performance against target is 6.1', 'air.png', True),
            SidebarData('', 'ATP to ancillary spend is 5.2', 'air.png', True)
        ]
        return active_alert_list

    def resolve_viewData(self, info):
        list1 = [
            VDListObject(title = 'Travel Manager Dashboard', icon = 'manager_active.png', link = '/travel'),
            VDListObject(title = 'Executive Dashboard', icon = 'manager_active.png', link = '/executive'),
            VDListObject(title = 'Card Deck', icon = 'tool_active.png', domo = True, link = 'https://www.domo.com/')
        ]
        list2 = [
            VDListObject(title = 'Air program analytics', icon = 'manager_disabled.png', link = '#'),
            VDListObject(title = 'Air program manager (A3)', icon = 'tool_disabled.png', link = '#')
        ]
        list3 = [
            VDListObject(title = 'Hotel program analytics', icon = 'manager_disabled.png', link = '#'),
            VDListObject(title = 'Hotel program manager (HPM)', icon = 'tool_disabled.png', link = '#')
        ]

        view_data_list = [
            ViewData(title = '360 analytics', icon = 'analytics_active.png', disabled = False, list = list1),
            ViewData(title = 'air', icon = 'air_disabled.png', disabled = True, list = list2),
            ViewData(title = 'hotel', icon = 'hotel_disabled.png', disabled = True, list = list3)
        ]

        return view_data_list

    def resolve_infoData(self, info):
        info_data_list = [
            ViewData(title = 'Webinar Name', description = 'Information about webinar', 
                icon = 'tool_disabled.png', disabled = True, button = 'register'),
            ViewData(title = 'Document Library', description = 'Information about library',
                icon = 'library_active.png', disabled = False),
            ViewData(title = 'Podcast', description = 'Information about podcast',
                icon = 'podcast_disabled.png', disabled = True, button = 'download'),
            ViewData(title = 'Item Name', description = 'Information about item',
                icon = 'tool_disabled.png', disabled = True, button = 'download')
        ]
        return info_data_list

schema = graphene.Schema(query=Query, mutation=MyMutations)
