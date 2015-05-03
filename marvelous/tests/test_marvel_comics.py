from marvelous.tests.base import MarvelTests
from betamax import Betamax


class TestMarvelComics(MarvelTests):

    def test_comic_by_id(self):
        with Betamax(self.api._session).use_cassette('ultron_comic'):
            result = self.api.comic(self.ultron_comic)
            self.assertIsInstance(result, dict)

    def test_comics_characters(self):
        with Betamax(self.api._session).use_cassette('comics_characters'):
            results = self.api.comics_characters(self.ultron_comic)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_comics_creators(self):
        with Betamax(self.api._session).use_cassette('comics_creators'):
            results = self.api.comics_creators(self.ultron_comic)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_comics_events(self):
        with Betamax(self.api._session).use_cassette('comics_events'):
            results = self.api.comics_events(self.ultron_comic)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_comics_stories(self):
        with Betamax(self.api._session).use_cassette('comics_stories'):
            results = self.api.comics_stories(self.ultron_comic)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])
