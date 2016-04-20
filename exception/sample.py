from base import APIException


class APIInternalError(APIException):
    """
    APIInternalError exceptions indicate that communications may have
    succeeded, but something went wrong inside the client.
    """
    message = 'love'

e = APIInternalError()
print e
