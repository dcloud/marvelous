from requests.exceptions import HTTPError


class APIError(HTTPError):
    pass
