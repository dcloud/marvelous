from marvelous.tests.base import MarvelTests

from marvelous.marvel import Marvel
from marvelous.exceptions import APIError


class TestMarvel(MarvelTests):

    def test_api_session_configuration(self):
        self.assertIsNotNone(self.api._session)
        self.assertEqual(self.api._session.headers['Accept-Encoding'], 'gzip')

    def test_needs_public_and_private_keys(self):
        unauthapi = Marvel()
        with self.assertRaises(APIError):
            unauthapi.comics()
