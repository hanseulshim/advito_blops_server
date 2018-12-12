import secrets
import base64
import hashlib


class Users:

    def __init__(self, db):

        """
        Constructs Users instance.
        Requires a references to an SQLAlchemy db client.
        """

        self.db = db


    """
    Represents the class that performs logic around a User.
    """

    def create(self, user):
        """
        Adds a user into the database
        When inserting the user, both base64(utf8(password + salt)) and base64(salt) are stored.
        """

        # Unpacks parameters
        username = user['username']
        password = user['password']
        email = user['email']

        # Gets password as bytes and generates a salt
        password_bytes = password.encode(encoding='UTF-8')
        salt_bytes = secrets.token_bytes(16)

        # Hashes salted password
        algo = hashlib.sha256()
        algo.update(password_bytes)
        algo.update(salt_bytes)
        hashed_password_bytes = algo.digest()

        # Converts both combined password and salt to base64-encoded strings
        hashed_password = base64 \
            .b64encode(hashed_password_bytes) \
            .decode('UTF-8')
        salt = base64 \
            .b64encode(salt_bytes) \
            .decode('UTF-8')

        # Returns mocked user
        return {
            "username": username,
            "email": email,
            "password": hashed_password,
            "salt": salt
        }
