import base64
import hashlib
import secrets


def salt_hash(password, salt=None):

    """
    Both hashes and salts a password.
    If salt is not supplied, salt will be created randomly.
    Salt is a base64 encoded string of bytes.
    Password is a string.
    Returns a tuple of the password and the salt that was used.
    """

    # Creates password bytes and either uses or calculates salt bytes.
    password_bytes = password.encode(encoding='UTF-8')
    if (salt is None):
        salt_bytes = secrets.token_bytes(16)
    else:
        salt_bytes = base64.b64decode(salt.encode(encoding='UTF-8'))

    # Hashes and salts password
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

    # Returns as tuple
    return (hashed_password, salt)
