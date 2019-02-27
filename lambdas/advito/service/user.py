import secrets
import base64
import hashlib
import json
from datetime import datetime
from datetime import timedelta
from advito.model.table import AdvitoUser, AdvitoUserSession, AdvitoApplicationRole, AdvitoUserRoleLink, AccessToken
from advito.util.string_util import salt_hash
from advito.error import LoginError, LogoutError, InvalidSessionError, ExpiredSessionError, NotFoundError, UnauthorizedError, TokenExpirationError
from advito.role import Role


def deserialize_user_create(user_create_json):

    """
    Utility function that parses a user_create json object and returns an AdvitoUser object
    :param user_create_json: Serialized user as a python dict.
    """

    # Deserializes user and returns it
    user = AdvitoUser (
        client_id = user_create_json.get('clientId'),
        username = user_create_json.get('username'),
        is_enabled = user_create_json.get('isEnabled'),
        address = user_create_json.get('address'),
        pwd = user_create_json.get('pwd'),
        name_last = user_create_json.get('nameLast'),
        name_first = user_create_json.get('nameFirst'),
        email = user_create_json.get('username'),
        phone = user_create_json.get('phone'),
    )
    return user


def deserialize_user(user_json):

    """
    Utility function that parses a user_create json object and returns an AdvitoUser object
    :param user_create_json: Serialized user as a python dict.
    """

    # Deserializes user and returns it
    user = AdvitoUser (
        id = user_json.get('id'),
        client_id = user_json.get('clientId'),
        address = user_json.get('address'),
        username = user_json.get('username'),
        is_enabled = user_json.get('isEnabled'),
        pwd = user_json.get('pwd'),
        name_last = user_json.get('nameLast'),
        name_first = user_json.get('nameFirst'),
        email = user_json.get('email'),
        phone = user_json.get('phone'),
        profile_picture_path = user_json.get('profilePicturePath', None),
        default_timezone = user_json.get('timezoneDefault', None),
        default_language = user_json.get('languageDefault', None),
        default_date_format = user_json.get('dateFormatDefault', None)
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
        'languageDefault': user.default_language,
        'dateFormatDefault': user.default_date_format
    }


class UserService:

    """
    Represents a service that performs operations on instances of `AdvitoUser`.
    Can insert users into database and select them.
    Operations utilize an SQLAlchemy session object, but never commit/rollback.
    That is the responsibility of the caller.
    """

    def __init__(self, session_duration_sec, reset_password_duration_hours):

        """
        Constructs a UserService instance.
        :param expiration_minutes: Real number representing the number of minutes a session lasts for.
        """
        self.session_duration_sec = session_duration_sec
        self.reset_password_duration_hours = reset_password_duration_hours


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


    def update(self, user, session):

        """
        Updates an AdvitoUser in the database.
        :param user: AdvitoUser object to update in the db. Assumes ID is present.
        :param session: SQLAlchemy session used for db operations.
        """

        user_serialized = {
            "username": user.username,
            "email": user.username,
            "name_last": user.name_last,
            "name_first": user.name_first,
            "profile_picture_path": user.profile_picture_path,
            "default_timezone": user.default_timezone,
            "default_date_format": user.default_date_format
        }

        # Updates user in db
        row_count = session \
            .query(AdvitoUser) \
            .filter(AdvitoUser.id == user.id) \
            .update(user_serialized)

        # Validates that a change occurred
        if row_count == 0:
            raise NotFoundError("Could not find user with specified id " + str(user.id))


    def update_any(self, user, session):

        """
        Updates an AdvitoUser in the database.
        :param user: AdvitoUser object to update in the db. Assumes ID is present.
        :param session: SQLAlchemy session used for db operations.
        """

        user_serialized = {
            "username": user.username,
            "email": user.username,
            "name_last": user.name_last,
            "name_first": user.name_first,
            "phone": user.phone,
            "address": user.address,
            "profile_picture_path": user.profile_picture_path,
            "is_enabled": user.is_enabled
        }

        # Updates user in db
        row_count = session \
            .query(AdvitoUser) \
            .filter(AdvitoUser.id == user.id) \
            .update(user_serialized)

        # Validates that a change occurred
        if row_count == 0:
            raise NotFoundError("Could not find user with specified id " + str(user.id))


    def get(self, session_token, session):

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
            .filter(AdvitoUser.username == username) \
            .first()

        # Checks that user exists
        if user is None:
            raise LoginError("User did not exist")

        # Checks that user is enabled
        if not user.is_enabled:
            raise LoginError("User is not enabled")

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


    def reset_password_start(self, email, session):

        """
        Begins process of resetting the user's password
        :param email: Email of user to reset password for.
        :return: Access token that should be sent in email.
        """

        # Gets user with email
        user = session \
            .query(AdvitoUser) \
            .filter(AdvitoUser.email == email) \
            .first()
        if user is None:
            raise NotFoundError("User with email '" + email + "' not found'")

        # Gets existing access token associated with user. Normally, it won't exist
        old_access_token = session \
            .query(AccessToken) \
            .filter(AccessToken.advito_user_id == user.id) \
            .filter(AccessToken.is_active == True) \
            .first()
        if old_access_token is not None:
            old_access_token.is_active = False

        # Creates access token
        token_str = base64.b64encode(secrets.token_bytes(16)).decode(encoding='UTF-8')
        expiration = datetime.now() + timedelta(hours = self.reset_password_duration_hours)
        token = AccessToken (
            advito_user_id = user.id,
            token_type = "FLYING/NORMAL",
            token = token_str,
            token_expiration = expiration
        )

        # Inserts into db and returns string
        session.add(token)
        return token_str


    def reset_password_end(self, access_token, new_password, session):

        """
        Finishes process of resetting the user's password
        :param access_token: Access token sent to the user.
        :param new_password: New password to set for user
        """

        # Gets user with email
        user_and_token = session \
            .query(AccessToken, AdvitoUser) \
            .join(AdvitoUser) \
            .filter(AccessToken.token == access_token) \
            .first()
        if user_and_token is None:
            raise NotFoundError("Access token not found")

        # Gets token and validates it
        token = user_and_token[0]
        if not token.is_active or datetime.now() > token.token_expiration:
            raise TokenExpirationError("Access token expired")

        # Gets user, hashes/salts new password and stores it alongside the salt that was used
        user = user_and_token[1]
        salt_and_hash = salt_hash(new_password)
        user.pwd = salt_and_hash[0]
        user.user_salt = salt_and_hash[1]

        # Expires token
        token.is_active = False


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
