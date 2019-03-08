from advito.model.table import AdvitoApplication, AdvitoApplicationFeature, Client, ClientFeatureLink
from advito.error import NotFoundError


def serialize_application_with_features(application_with_features):

    application = application_with_features[0]
    features = application_with_features[1]

    features_serialized = []
    for feature in features:
        features_serialized.append({
            "id": feature.id,
            "featureName": feature.feature_name,
            "featureTag": feature.feature_tag,
            "isActive": feature.is_active,
            "description": feature.description
        })

    """
    Serializes an instance of Application
    """
    return {
        "id": application.id,
        "applicationName": application.application_name,
        "applicationFull": application.application_full,
        "applicationTag": application.application_tag,
        "isActive": application.is_active,
        "description": application.description,
        "features": features_serialized
    }


def serialize_feature(feature):

    """
    Serializes an instance of AdvitoApplicationFeature
    """

    return {
        "id": feature.id,
        "applicationId": feature.advito_applicaiton_id,
        "featureName": feature.feature_name,
        "featureTag": feature.feature_tag,
        "isActive": feature.is_active,
        "description": feature.is_active
    }


class ApplicationService:


    def get_all(self, session):

        """
        Gets all AdvitoApplications from database
        :return: Tuple of AdvitoApplicaiton and a list of its AdvitoApplicationFeatures
        :param session: SQLAlchemy session used for db operations.
        """

        # Lists applications
        applications = session \
            .query(AdvitoApplication) \
            .all()

        # Gets all features
        applications_with_features = []
        for application in applications:
            features = session \
                .query(AdvitoApplicationFeature) \
                .filter(AdvitoApplicationFeature.advito_application_id == application.id) \
                .all()
            applications_with_features.append((application, features))

        # Done
        return applications_with_features


    def get_by_client(self, client_id, session):

        """
        Gets all applications that a client belongs to.
        Determines this by getting all features of the user and getting the applications those features belong to.
        Does not repeat features.
        :return: Tuple of AdvitoApplicaiton and a list of its AdvitoApplicationFeatures
        :param session: SQLAlchemy session used for db operations.
        """

        # Gets joined data from DB
        joined_data = session \
            .query(Client, AdvitoApplicationFeature, AdvitoApplication) \
            .join(ClientFeatureLink) \
            .join(AdvitoApplicationFeature) \
            .join(AdvitoApplication) \
            .all()

        # Gets applications with listed features.
        # Ensures that duplicate applcations are not found.
        applications_with_features_dict = {}
        applications_with_features = []
        for data in joined_data:
            feature = data[1]
            application = data[2]
            tuple = applications_with_features_dict.get(application.id)
            if tuple is None:
                tuple = (application, [])
                applications_with_features.append(tuple)
                applications_with_features_dict[application.id] = tuple
            tuple[1].append(feature)

        # Returns applications with their list of features as a list of tuples
        return applications_with_features
