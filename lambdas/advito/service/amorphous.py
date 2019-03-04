from sqlalchemy import text
from advito.model.table import AdvitoUser, AdvitoUserSession


def _client_id_of_session_token(session_token, session):
    user = session \
        .query(AdvitoUser) \
        .join(AdvitoUserSession) \
        .filter(AdvitoUserSession.session_token == session_token) \
        .first()
    return user.client_id


class AmorphousService:

    """
    Represents a service that returns amorphous data.
    Implemented in such a way due to time constraints.
    In the future, this class should be refactored into multiple classes and is not considered an ideal implementation.
    Functions generally are passthroughs for stored procedures in the database and merely return their json as a python dictionary.
    """

    def __init__(self):
        pass


    def udf_story_air(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_air'
        and simply returns the results.
        :param session_token: Token given by user to query by.
        :param session: Database session. Not to be confused with session_token.
        :return: JSON dictionary.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes function and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_air(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)


    def udf_story_air_airlines(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_air_airlines'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes function and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_air_airlines(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)


    def udf_story_air_cabins(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_air_cabins'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_air_cabins(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)


    def udf_story_air_routes(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_air_routes'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_air_routes(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)


    def udf_story_air_traffic(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_air_traffic'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_air_traffic(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)

    def udf_story_hotel(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_hotel'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_hotel(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)

    def udf_story_hotel_1(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_hotel_1'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_hotel_1(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)


    def udf_story_hotel_2(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_hotel_2'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_hotel_2(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)


    def udf_story_hotel_3(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_hotel_3'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_hotel_3(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)

    def udf_story_hotel_4(self, session_token, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_hotel_4'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Gets client id of user with that session token
        client_id = _client_id_of_session_token(session_token, session)

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_hotel_4(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)
