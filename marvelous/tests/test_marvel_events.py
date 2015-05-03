from marvelous.tests.base import MarvelTests
from betamax import Betamax


class TestMarvelEvents(MarvelTests):

    def test_event_by_id(self):
        with Betamax(self.api._session).use_cassette('age_of_ultron_event'):
            result = self.api.event(self.age_of_ultron_event)
            self.assertIsInstance(result, dict)

    def test_event_missing_id(self):
        with self.assertRaises(TypeError):
            self.api.event()

    def test_events_characters(self):
        with Betamax(self.api._session).use_cassette('events_characters'):
            results = self.api.events_characters(self.age_of_ultron_event)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_events_comics(self):
        with Betamax(self.api._session).use_cassette('events_comics'):
            results = self.api.events_comics(self.age_of_ultron_event)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_events_creators(self):
        with Betamax(self.api._session).use_cassette('events_creators'):
            results = self.api.events_creators(self.age_of_ultron_event)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_events_series(self):
        with Betamax(self.api._session).use_cassette('events_series'):
            results = self.api.events_series(self.age_of_ultron_event)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_events_stories(self):
        with Betamax(self.api._session).use_cassette('events_stories'):
            results = self.api.events_stories(self.age_of_ultron_event)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])
