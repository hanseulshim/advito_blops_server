import secrets
import base64
import hashlib
import json
from advito.model.table import AdvitoUser, AdvitoUserSession
from advito.util.string_util import saltHash
from advito.error import AdvitoError


def deserialize_user_create(user_json):

    """
    Utility function that parses a user json string and returns an AdvitoUser object
    :param user_json: User as dictionary.
    """

    # Salts and hashes password. Writes result back to json.
    salt_and_hash = saltHash(user_json['pwd'])
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
    UserService is a service that performs operations on instances of `AdvitoUser`.
    Can create users into database and extract them.
    When consuming users, expects them to come in as instances of `AdvitoUser`.
    Operations take a sessions as an argument and never commit themself.
    That is the responsibility of the caller.
    """

    def create(self, user, session):

        """
        Adds an AdvitoUser to the database
        When inserting the user, both base64(utf8(password + salt)) and base64(salt) are stored.
        :param user: AdvitoUser object to insert into the db.
        :param session: SQLAlchemy session used for db operations.
        """

        # Converts to AdvitoUser and saves it
        session.add(user)
        session.commit()


    def login(self, username, password, session):

        """
        Logs in an AdvitoUser..
        :param username: Username of the user
        :param password: Password of the user
        :param session: SQLAlchemy session used for db operations.
        :return: Login token as a str.
        """

        # Reads in user where username matches
        user = session \
            .query(AdvitoUser) \
            .filter_by(username=username) \
            .first()

        # Gets password and salt of existing user
        db_password = user.pwd
        db_salt = user.user_salt

        # Massages password
        hashed_password = saltHash(password, db_salt)[0]

        # Checks passwords match
        if hashed_password != db_password:
            raise AdvitoError("Passwords did not match")

        # Creates random base64-encoded token
        session_token = secrets.token_bytes(32)
        session_token = base64.b64encode(session_token)

        return "Temp token"
