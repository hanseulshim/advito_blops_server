import graphene
import json
import boto3
import base64
from blops_graphene_functions import *

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

    programPerformance = graphene.Field(DashboardDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    noChangeSince = graphene.Field(NoChangeSinceResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    personaList = graphene.Field(DashboardDataResponse, clientId=graphene.Int(), sessionToken=graphene.String())
    opportunities = graphene.Field (
        OpportunitiesResponse,
        clientId=graphene.Int(),
        sessionToken=graphene.String(),
        limit=graphene.Int(),
        cursor=graphene.Int()
    )
    riskAreas = graphene.Field (
        RiskAreasResponse,
        clientId=graphene.Int(),
        sessionToken=graphene.String(),
        limit=graphene.Int(),
        cursor=graphene.Int()
    )
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
