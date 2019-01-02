class AdvitoError(Exception):
    pass

class LoginError(AdvitoError):
    pass

class LogoutError(AdvitoError):
    pass

class BadRequestError(AdvitoError):
    pass

class InvalidSessionError(AdvitoError):
    pass

class ExpiredSessionError(AdvitoError):
    pass

class NotFoundError(AdvitoError):
    pass
