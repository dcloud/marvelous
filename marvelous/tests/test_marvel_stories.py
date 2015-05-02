import unittest


class TestMarvelStories(unittest.TestCase):

    def test_story_by_id(self):
        result = self.api.story(self.story)
        self.assertIsInstance(result, dict)

    def test_story_missing_id(self):
        with self.assertRaises(TypeError):
            self.api.story()

    def test_stories_characters(self):
        results = self.api.stories_characters(self.story)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_stories_comics(self):
        results = self.api.stories_comics(self.story)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_stories_creators(self):
        results = self.api.stories_creators(self.story)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_stories_events(self):
        results = self.api.stories_events(self.story)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_stories_series(self):
        results = self.api.stories_series(self.story)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

