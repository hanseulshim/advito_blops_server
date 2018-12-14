import secrets
import base64
import hashlib
import json
from util.string_util import saltHash


# Acquires DB classes necessary for subsequent operations
advito_user = Base.classes.advito_user
advito_user_session = Base.classes.advito_user_session


def parse_new_user(user_json):

    """
    Utility function that parses a user json string and returns an advito_user object
    """

    # Converts json string to dictionary
    user_json = json.loads(user_body)

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
    user_dict = json.loads(user_json)




class UserService:

    """
    UserService is a service that performs operations on instances of `advito_user`.
    Can create users into database and extract them.
    When consuming users, expects them to come in as instances of `advito_user`.
    Operations take a sessions as an argument and never commit themself.
    That is the responsibility of the caller.
    """

    def create(self, user, session):

        """
        Adds an advito_user to the database
        When inserting the user, both base64(utf8(password + salt)) and base64(salt) are stored.
        :param user: advito_user object to insert into the db.
        :param session: SQLAlchemy session used for db operations.
        """

        # Converts to advito_user and saves it
        session.add(usr)
        session.commit()
