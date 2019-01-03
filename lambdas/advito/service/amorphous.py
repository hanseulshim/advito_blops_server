from sqlalchemy import text

class AmorphousService:

    """
    Represents a service that returns amorphous data.
    Implemented in such a way due to time constraints.
    In the future, this class should be refactored into classes and is not considered an ideal implementation.
    Functions generally are passthroughs for stored procedures in the database and merely return their json as
    a python dictionary.
    """

    def __init__(self):
        pass


    def udf_story_air(self, client_id, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_air'
        and simply returns the results.
        :param client_id: Integer representing the client id.
        :param session: SQLAlchemy session used for DB operations.
        :return: JSON dictionaory.
        """

        # Executes funciton and gets row proxy.
        rowproxy = session.execute (
            "SELECT udf_story_air(:client_id)",
            { "client_id": client_id }
        ).first()

        # Turns to dictionary and returns
        return dict(rowproxy)
