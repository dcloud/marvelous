import requests
from urllib.parse import urlunsplit
import hashlib
from datetime import datetime

from marvelous.utils import ResponseDict, ResponseList


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

        def nowtimestamp():
            return datetime.utcnow().strftime('%f')
        self._create_ts_string = nowtimestamp

    def _generate_url(self, endpoint_path):
        url_path = '{}/{}/{}'.format(Marvel.api_version, Marvel.access_type, endpoint_path)
        url_parts = (Marvel.scheme, Marvel.domain, url_path, '', '')
        return urlunsplit(url_parts)

    def _get(self, endpoint, params=None):
        params = params or {}
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

    def character(self, character_id, params=None):
        return self._get('character/{}'.format(character_id), params=params)

    def characters(self, params=None):
        return self._get('characters', params=params)
