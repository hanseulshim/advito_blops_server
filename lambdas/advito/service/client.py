from advito.model.table import Client


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
        "isActive": client.is_active,
        "industry": client.industry,
        "defaultCurrencyCode": client.default_currency_code,
        "defaultDistanceUnits": client.default_distance_units,
        "description": client.description
    }


def deserialize_client(client_json):

    """
    Serializes a client json to a Client db object.
    """

    return Client (
        id = client_json["id"],
        client_name = client_json["clientName"],
        client_name_full = client_json["clientNameFull"],
        client_tag = client_json["clientTag"],
        is_active = client_json["isActive"],
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
            "is_active": client.is_active,
            "industry": client.industry,
            "default_currency_code": client.default_currency_code,
            "default_distance_units": client.default_distance_units,
            "description": client.description
        }

        # Updates in database
        session \
            .query(Client) \
            .fliter(Client.id == client['id']) \
            .update(client_serialized)
