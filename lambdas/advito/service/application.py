from advito.model.table import Client, ClientDivision
from advito.error import NotFoundError


class ApplicationService:

    def get_all(self, session):

        """
        Gets all applications
        :param user_id: Id of AdvitoUser to create role for.
        :param role: Name of AdvitoApplicationRole to give AdvitoUser.
        :param session: SQLAlchemy session used for db operations.
        """

        link = AdvitoUserRoleLink (
            advito_user_id = user_id,
            advito_role_id = role.value
        )
        session.add(link)
