import os
import betamax
from marvelous.tests.utils import EndpointQueryMatcher


betamax.Betamax.register_request_matcher(EndpointQueryMatcher)

CASSETTES_PATH = 'marvelous/tests/cassettes'

if not os.path.exists(CASSETTES_PATH):
    os.makedirs(CASSETTES_PATH)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'marvelous/tests/cassettes/'
    config.re_record_interval = 2/24  # Rerecord every 2 hours be default
    config.default_cassette_options['match_requests_on'] = ['host', 'method', 'endpoint']
