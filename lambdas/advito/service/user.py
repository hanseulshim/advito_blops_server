import secrets
import base64
import hashlib
import json
from datetime import datetime
from datetime import timedelta
from advito.model.table import AdvitoUser, AdvitoUserSession, AdvitoApplicationRole, AdvitoUserRoleLink
from advito.util.string_util import salt_hash
from advito.error import LoginError, LogoutError, InvalidSessionError, ExpiredSessionError, NotFoundError, UnauthorizedError
from advito.role import Role


def deserialize_user_create(user_create_json):

    """
    Utility function that parses a user_create json object and returns an AdvitoUser object
    :param user_create_json: Serialized user as a python dict.
    """

    # Deserializes user and returns it
    user = AdvitoUser (
        client_id = user_create_json['clientId'],
        username = user_create_json['username'],
        pwd = user_create_json['pwd'],
        name_last = user_create_json['nameLast'],
        name_first = user_create_json['nameFirst'],
        email = user_create_json['email'],
        phone = user_create_json['phone'],
        profile_picture_path = user_create_json.get('profilePicturePath', None),
        default_timezone = user_create_json.get('timezoneDefault', None),
        default_language = user_create_json.get('languageDefault', None)
    )
    return user


def serialize_user(user):

    """
    Serializes a user as a python dict.
    Does not include hashed/salted password.
    :param user: AdvitoUser to serialize.
    """

    return {
        'id': user.id,
        'clientId': user.client_id,
        'username': user.username,
        'nameLast': user.name_last,
        'nameFirst': user.name_first,
        'email': user.email,
        'phone': user.phone,
        'profilePicturePath': user.profile_picture_path,
        'timezoneDefault': user.default_timezone,
        'languageDefault': user.default_language
    }



class UserService:

    """
    Represents a service that performs operations on instances of `AdvitoUser`.
    Can insert users into database and select them.
    Operations utilize an SQLAlchemy session object, but never commit/rollback.
    That is the responsibility of the caller.
    """

    def __init__(self, session_duration_sec):

        """
        Constructs a UserService instance.
        :param expiration_minutes: Real number representing the number of minutes a session lasts for.
        """
        self.session_duration_sec = session_duration_sec


    def create(self, user, session):

        """
        Adds an AdvitoUser to the database
        When inserting the user, both base64(utf8(password + salt)) and base64(salt) are stored.
        :param user: AdvitoUser object to insert into the db.
        :param session: SQLAlchemy session used for db operations.
        """

        # Salts and hashes password. Writes result back to object.
        salt_and_hash = salt_hash(user.pwd)
        user.pwd = salt_and_hash[0]
        user.user_salt = salt_and_hash[1]

        # Converts to AdvitoUser and saves it
        session.add(user)


    def get_by_session_token(self, session_token, session):

        """
        Gets an AdvitoUser by session_token.
        :param session_token: Token given by user to query by.
        :param session: Database session. Not to be confused with session_token.
        """

        # Gets id of user with given session token
        user_session = session \
            .query(AdvitoUserSession) \
            .filter_by(session_token=session_token) \
            .first()
        if user_session is None:
            raise NotFoundError("Could not find session token.")

        # Gets user using id found
        user_id = user_session.advito_user_id
        user = session \
            .query(AdvitoUser) \
            .filter_by(id=user_id) \
            .first()
        if user is None:
            raise NotFoundError("Session token was found, but no associated user was found. This should not happen.")

        # Done
        return user



    def get_by_username(self, username, session):

        """
        Gets an AdvitoUser by username
        :param username: Username of the user to get
        :param session: SQLAlchemy session used for db operations.
        :return: AdvitoUser instance.
        """

        user = session \
            .query(AdvitoUser) \
            .filter_by(username=username) \
            .first()
        if user is None:
            raise NotFoundError("Could not find user '{}'".format(username))
        return user



    def login(self, username, password, session):

        """
        Logs in an AdvitoUser.
        :param username: Username of the user
        :param password: Password of the user
        :param session: SQLAlchemy session used for db operations.
        :return: A tuple of the AdvitoUser and session string.
        """

        # Reads in user where username matches
        user = session \
            .query(AdvitoUser) \
            .filter_by(username=username) \
            .first()

        # Checks that user exists
        if user is None:
            raise LoginError("User did not exist")

        # Gets password and salt of existing user
        db_password = user.pwd
        db_salt = user.user_salt

        # Massages password
        hashed_password = salt_hash(password, db_salt)[0]

        # Checks passwords match
        if hashed_password != db_password:
            raise LoginError("Passwords did not match")

        # Creates user session in db and returns it.
        # Discards existing user session if there was one.
        user_session = self._create_session(user, session)
        return (user, user_session)


    def logout(self, session_token, session):

        """
        Logs out an AdvitoUser.
        :param username: String token string of user to log out.
        :param session: SQLAlchemy session used for db operations.
        """

        # Finds session to expire
        db_session = session \
            .query(AdvitoUserSession) \
            .filter(AdvitoUserSession.session_token == session_token) \
            .filter(AdvitoUserSession.session_end == None) \
            .first()

        # Ensures session exists
        if db_session == None:
            raise LogoutError("User not logged in. Logout is impossible.")

        # Expires session
        session.query(AdvitoUserSession) \
            .filter(AdvitoUserSession.session_token == session_token) \
            .filter(AdvitoUserSession.session_end == None) \
            .update({"session_end" : datetime.now()}, synchronize_session=False)




    def validate_logged_in(self, session_token, session, roles=[]):

        """
        Validates that an AdvitoUser is logged in.
        If logged in, expiration_time in database will be updated and method will exit normally.
        If they are not, this method will raise an error.
        :param session_token: Session token to validate logged-in status.
        :param session: SQLAlchemy session used for db operations.
        :param roles: List of Role enums that user must have in order be considered validated. Optional.
        :return: True if user is logged in. False otherwise.
        """

        # Gets latest session for user in the database
        user_session = session \
            .query(AdvitoUserSession) \
            .filter_by(session_token = session_token) \
            .filter(AdvitoUserSession.session_end == None) \
            .first()

        # Checks that there was a session and that it matches supplied token.
        if user_session is None:
            raise InvalidSessionError("No session found")

        # Check that session is not expired.
        if datetime.now() >= user_session.session_expiration:
            raise ExpiredSessionError("Session expired")

        # Makes db call if certain roles are required
        if len(roles) > 0:

            # Determines the roles this user has. If they don't contain all that is in 'roll_ids', the user is not authenticated.
            user_roles_query = session \
                .query(AdvitoApplicationRole) \
                .join(AdvitoUserRoleLink) \
                .join(AdvitoUser) \
                .join(AdvitoUserSession) \
                .filter(AdvitoUserSession.session_token == session_token)
            user_roles = user_roles_query.all()
            user_roles = [Role(user_role.id) for user_role in user_roles]
            if not set(roles).issubset(user_roles):
                role_names = [role.name for role in roles]
                user_role_names = [user_role.name for user_role in user_roles]
                raise UnauthorizedError("User had role(s) " + str(user_role_names) + " but must have role(s) " + str(role_names))


        # Update session in DB
        duration = timedelta(seconds = user_session.session_duration_sec)
        session \
            .query(AdvitoUserSession) \
            .filter_by(session_token = session_token) \
            .filter(AdvitoUserSession.session_end == None) \
            .update({"session_expiration": datetime.now() + duration})


    def _create_session(self, user, session):

        """
        Generates a session for the specified user
        Creates it in the database if it does not exist or the latest one is expired.
        :param user: User to generate session for.
        :param session: SQLAlchemy session used for db operations.
        """

        # Expires existing session for this user if it exists.
        # Otherwise, does nothing.
        session \
            .query(AdvitoUserSession) \
            .filter(AdvitoUserSession.advito_user_id == user.id) \
            .filter(AdvitoUserSession.session_end == None) \
            .update({"session_end" : datetime.now()}, synchronize_session=False)

        # Makes session that will be used in other calls
        user_session = AdvitoUserSession()
        user_session.advito_user_id = user.id
        user_session.session_token = base64 \
            .b64encode(secrets.token_bytes(16)) \
            .decode(encoding='UTF-8')
        user_session.session_start = datetime.now()
        user_session.session_end = None
        user_session.session_duration_sec = self.session_duration_sec
        user_session.session_type = None
        user_session.session_expiration = datetime.now() + timedelta(seconds=self.session_duration_sec)
        user_session.session_note = None

        #  Inserts session
        session.add(user_session)

        # Returns session
        return user_session
