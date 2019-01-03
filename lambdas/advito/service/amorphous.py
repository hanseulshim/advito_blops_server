class Amorphous:

    """
    Represents a service that returns amorphous data.
    Implemented in such a way due to time constraints.
    In the future, this class should be refactored into classes and is not considered an ideal implementation.
    Functions generally are passthroughs for stored procedures in the database and merely return their json as
    a python dictionary.
    """

    def __init__(self):
        pass


    def udf_story_air(self, session):

        """
        Passthrough function that invokes the postgres function 'udf_story_air'
        and simply returns the results.
        """
        pass
