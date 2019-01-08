import graphene
import json
import boto3
import base64

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
    delta = graphene.Int()
    percent = graphene.Float()
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