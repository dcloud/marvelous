from urllib import parse
from betamax import BaseMatcher


class EndpointQueryMatcher(BaseMatcher):
    name = 'endpoint'

    def endpoint_parts(self, url):
        scheme, netloc, path, query, _ = parse.urlsplit(url)
        identity_dict = parse.parse_qs(query)
        common_params = ('apikey', 'hash', 'ts')
        for p in common_params:
            if p in identity_dict:
                del identity_dict[p]
        return identity_dict

    def match(self, request, recorded_request):
        request_url, recorded_url = request.url, recorded_request['uri']
        return self.endpoint_parts(request_url) == self.endpoint_parts(recorded_url)
