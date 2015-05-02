import requests
from urllib.parse import urlunsplit
import hashlib
from datetime import datetime

from marvelous.utils import ResponseDict, ResponseList
from marvelous.exceptions import APIError
from marvelous.__init__ import __version__


class Marvel(object):
    """Marvel Comics API bindings"""
    scheme = 'https'
    domain = 'gateway.marvel.com'
    api_version = 'v1'
    access_type = 'public'

    def __init__(self, private_key=None, public_key=None):
        super(Marvel, self).__init__()
        self.private_key = private_key
        self.public_key = public_key
        self._session = requests.Session
        self._session.headers = {
            'Accept-Encoding': 'gzip',
            'User-Agent': 'Marvelous Python Client/{}'.format(__version__)
        }

        def singular_for_path(path):
            singulars = dict((
                ('series', 'series_with_id'),
                ('stories', 'story'),
            ))
            return singulars.get(path, path.rstrip('s'))

        def make_endpoint(path, subpath=None, requires_id=False):
            parts = (path,)
            if requires_id or subpath:
                parts += ('{}',)
            if subpath:
                parts += (subpath,)
            endpoint = '/'.join(parts)

            def api_object_id_endpoint(object_id, **filters):
                return self._get(endpoint.format(object_id), **filters)

            def api_basic_endpoint(**filters):
                return self._get(endpoint, **filters)

            endpoint_func = api_object_id_endpoint if requires_id else api_basic_endpoint

            if subpath:
                endpoint_func.__doc__ = "API endpoint for `{}`, filtered by `{}`".format(subpath, path)
            else:
                endpoint_func.__doc__ = "API endpoint for `{}`.".format(singular_for_path(path))
            if requires_id:
                endpoint_func.__doc__ += " Requires an object id."
            return endpoint_func

        endpoints = (
            ('characters', ('comics', 'events', 'series', 'stories')),
            ('comics', ('characters', 'creators', 'events', 'stories')),
            ('creators', ('comics', 'events', 'series', 'stories')),
            ('events', ('characters', 'comics', 'creators', 'series', 'stories')),
            ('series', ('characters', 'comics', 'creators', 'events', 'stories')),
            ('stories', ('characters', 'comics', 'creators', 'events', 'series'))
        )

        for path, subset in endpoints:
            setattr(self, path, make_endpoint(path))
            singular_endpoint = singular_for_path(path)
            setattr(self, singular_endpoint, make_endpoint(path, requires_id=True))
            for subpath in subset:
                method = '{}_{}'.format(path, subpath)
                setattr(self, method, make_endpoint(path, subpath, requires_id=True))

        def nowtimestamp():
            return datetime.utcnow().strftime('%f')
        self._create_ts_string = nowtimestamp

    def _generate_url(self, endpoint_path):
        url_path = '{}/{}/{}'.format(Marvel.api_version, Marvel.access_type, endpoint_path)
        url_parts = (Marvel.scheme, Marvel.domain, url_path, '', '')
        return urlunsplit(url_parts)

    def _get(self, endpoint, **filters):
        params = filters or {}
        if not (self.private_key or self.public_key):
            raise Exception('Both `private_key` and `public_key` must be set')
        else:
            ts = self._create_ts_string()
            h = hashlib.md5(bytes(ts, 'utf-8'))
            h.update(bytes(self.private_key, 'utf-8'))
            h.update(bytes(self.public_key, 'utf-8'))
            params.update({
                    'ts': ts,
                    'hash': h.hexdigest(),
                    'apikey': self.public_key
            })
            api_url = self._generate_url(endpoint)
            response = requests.get(api_url, params=params)
            if response.ok:
                return self._unwrap_response_json(response.json())
            else:
                try:
                    error_obj = response.json()
                    error_message = error_obj.get('status')
                    raise APIError(error_message)
                except ValueError:
                    raise requests.exceptions.HTTPError()

    def _unwrap_response_json(self, response_json):
        if 'data' in response_json and 'results' in response_json['data']:
            raw_results = response_json['data'].pop('results')
            meta_info = response_json.copy()
            if len(raw_results) > 1:
                return ResponseList(data=raw_results, meta=meta_info)
            else:
                return ResponseDict(data=raw_results[0], meta=meta_info)
        else:
            raise Exception('Unable to unwrap JSON response.')
