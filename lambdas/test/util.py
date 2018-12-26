import base64
import secrets

def randstr():

    """
    Generates random 16-byte string
    """

    bytes = secrets.token_bytes(16)
    string = base64.b64encode(bytes).decode(encoding='UTF-8')
    return '-test-' + string
