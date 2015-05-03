from marvelous.tests.base import MarvelTests
from betamax import Betamax


class TestMarvelCreators(MarvelTests):

    def test_creator_by_id(self):
        with Betamax(self.api._session).use_cassette('bendis'):
            result = self.api.creator(self.bendis)
            self.assertIsInstance(result, dict)

    def test_creators_comics(self):
        with Betamax(self.api._session).use_cassette('creators_comics'):
            results = self.api.creators_comics(self.bendis)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_creators_events(self):
        with Betamax(self.api._session).use_cassette('creators_events'):
            results = self.api.creators_events(self.bendis)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_creators_series(self):
        with Betamax(self.api._session).use_cassette('creators_series'):
            results = self.api.creators_series(self.bendis)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_creators_stories(self):
        with Betamax(self.api._session).use_cassette('creators_stories'):
            results = self.api.creators_stories(self.bendis)
            self.assertEqual(len(results), results._meta['data']['count'])
