from advito.model.table import Client, ClientDivision
from advito.error import NotFoundError


def serialize_client(client):

    """
    Deserializes a Client object into a json dict
    """

    return {
        "id": client.id,
        "clientName": client.client_name,
        "clientNameFull": client.client_name_full,
        "clientTag": client.client_tag,
        "gcn": client.gcn,
        "lanyonClientCode": client.lanyon_client_code,
        "isActive": client.is_active,
        "logoPath": client.logo_path,
        "industry": client.industry,
        "defaultCurrencyCode": client.default_currency_code,
        "defaultDistanceUnits": client.default_distance_units,
        "description": client.description
    }

def serialize_client_division(client_division):

    """
    Deserializes a ClientDivision object into a json dict.
    """

    return {
        "id": client_division.id,
        "clientId": client_division.client_id,
        "divisionName": client_division.division_name,
        "divisionNameFull": client_division.division_name_full,
        "divisionTag": client_division.division_tag,
        "gcn": client_division.gcn,
        "isActive": client_division.is_active,
        "description": client_division.description
    }

def deserialize_client_division_create(client_division_json):
    return ClientDivision (
        client_id = client_division_json["clientId"],
        division_name = client_division_json["divisionName"],
        division_name_full = client_division_json["divisionNameFull"],
        division_tag = client_division_json["divisionTag"],
        gcn = client_division_json["gcn"],
        is_active = client_division_json["isActive"],
        description = client_division_json["description"],
    )

def deserialize_client_division(client_division_json):

    return ClientDivision (
        id = client_division_json["id"],
        division_name = client_division_json["divisionName"],
        division_name_full = client_division_json["divisionNameFull"],
        division_tag = client_division_json["divisionTag"],
        gcn = client_division_json["gcn"],
        is_active = client_division_json["isActive"],
        description = client_division_json["description"],
    )

def deserialize_client(client_json):

    """
    Serializes a client json to a Client db object.
    """

    return Client (
        id = client_json["clientId"],
        client_name = client_json["clientName"],
        client_name_full = client_json["clientNameFull"],
        client_tag = client_json["clientTag"],
        gcn = client_json["gcn"],
        lanyon_client_code = client_json["lanyonClientCode"],
        is_active = client_json["isActive"],
        logo_path = client_json["logoPath"],
        industry = client_json["industry"],
        default_currency_code = client_json["defaultCurrencyCode"],
        default_distance_units = client_json["defaultDistanceUnits"],
        description = client_json["description"]
    )

def deserialize_client_create(client_json):

    """
    Serializes a client json to a Client db object.
    """

    return Client (
        client_name = client_json["clientName"],
        client_name_full = client_json["clientNameFull"],
        client_tag = client_json["clientTag"],
        gcn = client_json["gcn"],
        lanyon_client_code = client_json["lanyonClientCode"],
        is_active = client_json["isActive"],
        logo_path = client_json["logoPath"],
        industry = client_json["industry"],
        default_currency_code = client_json["defaultCurrencyCode"],
        default_distance_units = client_json["defaultDistanceUnits"],
        description = client_json["description"]
    )


class ClientService:


    def get_all(self, session):

        """
        Gets all clients stored in the DB
        :param session: SQLAlchemy session used for db operations.
        :return: All Clients stored in db
        """

        return session \
            .query(Client) \
            .all()


    def get_divisions(self, client_id, session):

        """
        Gets all divisions of a given client
        :param client_id: Id of client to query for.
        :param session: SQLAlchemy session used for db operations.
        :return: ClientDivision instance.
        """

        return session \
            .query(ClientDivision) \
            .filter(ClientDivision.client_id == client_id) \
            .all()

    def create_division(self, client_division, session):

        """
        Creates a new a ClientDivision
        :param client_division: ClientDivision to create.
        :param session: SQLAlchemy session used for db operations.
        """
        session.add(client_division)


    def update_division(self, client_division, session):

        """
        Updates a ClientDivision
        :param client_division: ClientDivision to update.
        :param session: SQLAlchemy session used for db operations.
        """

        # Serializes division for updating purposes
        serialized = {
            "division_name": client_division.division_name,
            "division_name_full": client_division.division_name_full,
            "is_active": client_division.is_active,
            "division_tag": client_division.division_tag,
            "gcn": client_division.gcn,
            "description": client_division.description
        }

        # Updates in database
        rowcount = session \
            .query(ClientDivision) \
            .filter(ClientDivision.id == client_division.id) \
            .update(serialized)

        # Validates that a change occurred
        if rowcount == 0:
            raise NotFoundError("Could not find division with id " + str(client_division.id))


    def create(self, client, session):

        """
        Creates a client int he DB.
        :param client: Client to create.
        :param session: SQLAlchemy session used for db operations.
        :return: Client created.
        """
        session.add(client)


    def update(self, client, session):

        """
        Updates an existing client in the DB
        :param client: Client to update data for.
        :param session: SQLAlchemy session used for db operations.
        :return: All Clients stored in db
        """

        # Serializes request as dictionary
        client_serialized = {
            "client_name": client.client_name,
            "client_name_full": client.client_name_full,
            "client_tag": client.client_tag,
            "gcn": client.gcn,
            "lanyon_client_code": client.lanyon_client_code,
            "is_active": client.is_active,
            "industry": client.industry,
            "default_currency_code": client.default_currency_code,
            "default_distance_units": client.default_distance_units,
            "description": client.description
        }

        # Updates in database
        rowcount = session \
            .query(Client) \
            .filter(Client.id == client.id) \
            .update(client_serialized)

        # Validates that a change occurred
        if rowcount == 0:
            raise NotFoundError("Could not find client specified with id " + str(client.id))
