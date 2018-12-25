import secrets
import base64
import hashlib
import json
from datetime import datetime
from datetime import timedelta
from advito.model.table import AdvitoUser, AdvitoUserSession
from advito.util.string_util import salt_hash
from advito.error import LoginError, InvalidSessionError, ExpiredSessionError


def deserialize_user_create(user_json):

    """
    Utility function that parses a user_create json object and returns an AdvitoUser object
    :param user_json: Serialized user as a python dict.
    """

    # Salts and hashes password. Writes result back to json.
    salt_and_hash = salt_hash(user_json['pwd'])
    user_json['pwd'] = salt_and_hash[0]
    user_json['user_salt'] = salt_and_hash[1]

    # Sets default values
    user_json['is_enabled'] = True
    user_json['must_change_pwd'] = False
    user_json['pwd_expiration'] = '01/01/2024'
    user_json['created'] = '01/01/1900'
    user_json['modified'] = '12/12/2018'

    # Returns deserialized user
    return AdvitoUser(**user_json)



class UserService:

    """
    Represents a service that performs operations on instances of `AdvitoUser`.
    Can insert users into database and select them.
    Operations utilize an SQLAlchemy session object, but never commit.
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

        # Converts to AdvitoUser and saves it
        session.add(user)


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


    def validate_logged_in(self, session_token, session):

        """
        Validates that an AdvitoUser is logged in.
        If logged in, expiration_time in database will be updated and method will exit normally.
        If they are not, this method will raise an error.
        :param session_token: Session token to validate logged-in status.
        :param session: SQLAlchemy session used for db operations.
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