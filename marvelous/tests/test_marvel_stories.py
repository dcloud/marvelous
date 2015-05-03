from marvelous.tests.base import MarvelTests
from betamax import Betamax


class TestMarvelStories(MarvelTests):

    def test_story_by_id(self):
        with Betamax(self.api._session).use_cassette('story_by_id'):
            result = self.api.story(self.story)
            self.assertIsInstance(result, dict)

    def test_story_missing_id(self):
        with self.assertRaises(TypeError):
            self.api.story()

    def test_stories_characters(self):
        with Betamax(self.api._session).use_cassette('stories_characters'):
            results = self.api.stories_characters(self.story)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_stories_comics(self):
        with Betamax(self.api._session).use_cassette('stories_comics'):
            results = self.api.stories_comics(self.story)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_stories_creators(self):
        with Betamax(self.api._session).use_cassette('stories_creators'):
            results = self.api.stories_creators(self.story)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_stories_events(self):
        with Betamax(self.api._session).use_cassette('stories_events'):
            results = self.api.stories_events(self.story)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

    def test_stories_series(self):
        with Betamax(self.api._session).use_cassette('stories_series'):
            results = self.api.stories_series(self.story)
            self.assertIsInstance(results, list)
            self.assertEqual(len(results), results._meta['data']['count'])

