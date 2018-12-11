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

    def create(user):
        """
        Adds a user into the database
        When inserting the user, both base64(utf8(password + salt)) and base64(salt) are stored.
        """

        # Unpacks parameters
        username = user['username']
        password = user['password']
        email = user['email']

        # Salts password
        password_bytes = password.encode(encoding='UTF-8')
        salt_bytes = secrets.token_bytes(16)
        combined_bytes = password_bytes + salt_bytes

        # Converts both combined password and salt to base64-encoded strings
        combined = base64.b64encode(combined_bytes)
        salt = base64.b64encode(salt_bytes)

        # Stores user in db
        connection_str = os.environ['DB_CONNECTION']
        print(connection_str)
