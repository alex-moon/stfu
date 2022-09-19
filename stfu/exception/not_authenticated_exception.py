from .stfu_exception import StfuException


class NotAuthenticatedException(StfuException):
    code = 403

    def __init__(self, token: str):
        super().__init__("Invalid token: [%s]" % token)
