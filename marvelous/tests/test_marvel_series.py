from marvelous.tests.base import MarvelTests
from betamax import Betamax


class TestMarvelSeries(MarvelTests):

    def test_series_by_id(self):
        with Betamax(self.api._session).use_cassette('avengers_series'):
            result = self.api.series_with_id(self.avengers_series)
            self.assertIsInstance(result, dict)

    def test_series_missing_id(self):
        with self.assertRaises(TypeError):
            self.api.series_with_id()

    def test_search_series_titleStartsWith(self):
        with Betamax(self.api._session).use_cassette('series_titleStartsWith'):
            results = self.api.series(titleStartsWith='What if')
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_series_characters(self):
        with Betamax(self.api._session).use_cassette('series_characters'):
            results = self.api.series_characters(self.avengers_series)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_series_comics(self):
        with Betamax(self.api._session).use_cassette('series_comics'):
            results = self.api.series_comics(self.avengers_series)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_series_creators(self):
        with Betamax(self.api._session).use_cassette('series_creators'):
            results = self.api.series_creators(self.avengers_series)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_series_events(self):
        with Betamax(self.api._session).use_cassette('series_events'):
            results = self.api.series_events(self.avengers_series)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_series_stories(self):
        with Betamax(self.api._session).use_cassette('series_stories'):
            results = self.api.series_stories(self.avengers_series)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])
