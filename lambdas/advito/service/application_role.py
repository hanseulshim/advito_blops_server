import json
from advito.model.table import AdvitoUser, AdvitoUserRoleLink, AdvitoApplicationRole
from advito.error import NotFoundError


def serialize_application_role(role):

    """
    Serializes an AdvitoApplicationRole as a python dict.
    """
    return {
        "id": role.id,
        "advitoApplicationId": role.advito_application_id,
        "roleName": role.role_name,
        "roleTag": role.role_tag,
        "isActive": role.is_active,
        "description": role.description,
        "is_assignable": role.is_assignable
    }


class ApplicationRoleService:

    """
    Represents a service that performs operations on instances of `AdvitoApplicationRole`.
    Can insert users into database and select them.
    Operations utilize an SQLAlchemy session object, but never commit/rollback.
    That is the responsibility of the caller.
    """

    def __init__(self, user_service):

        """
        Constructs the ApplicationRoleService
        :param user_service: UserService dependency.
        """
        self.user_service = user_service


    def get_all_for(self, session_token, session):

        """
        Gets all ApplicationRoleServices for a given AdvitoUser
        :param session_token: Session token for an AdvitoUser. Used for determining of that user has the right privileges to query this function.
        :param session: SQLAlchemy session used for db operations.
        """

        # Gets user of token
        user = self \
            .user_service \
            .get_by_session_token(session_token, session)

        # Returns tuple of users and their roles
        return session \
            .query(AdvitoUser, AdvitoApplicationRole) \
            .join(AdvitoUserRoleLink) \
            .join(AdvitoApplicationRole) \
            .all()
