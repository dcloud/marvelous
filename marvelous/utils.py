class ResponseDict(dict):
    """
    ResponseDict provides a dictionary representation of an API response item along
    with a _meta dictionary that contains information about the query results.
    This could include result count and pagination details.
    """
    def __init__(self, data={}, meta=None):
        dict.__init__(self, data)
        self._meta = meta


class ResponseList(list):
    """
    ResponseList provides an iterable of API results along with a _meta
    dictionary that contains information about the query results. This could
    include result count and pagination details.
    """
    def __init__(self, data=[], meta=None):
        list.__init__(self, data)
        self._meta = meta
