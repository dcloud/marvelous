import unittest
import os

from marvelous.marvel import Marvel
from marvelous.exceptions import APIError

MARVEL_API_PUBLIC_KEY = os.environ.get('MARVEL_API_PUBLIC_KEY', '')
MARVEL_API_PRIVATE_KEY = os.environ.get('MARVEL_API_PRIVATE_KEY', '')


class TestMarvel(unittest.TestCase):

    def setUp(self):
        self.api = Marvel(public_key=MARVEL_API_PUBLIC_KEY, private_key=MARVEL_API_PRIVATE_KEY)
        self.wolverine = 1009718
        self.doop = 1009279
        self.bendis = 24
        self.story = 15

    def test_api_session_configuration(self):
        self.assertIsNotNone(self.api._session)
        self.assertEqual(self.api._session.headers['Accept-Encoding'], 'gzip')

    def test_needs_public_and_private_keys(self):
        unauthapi = Marvel()
        with self.assertRaises(APIError):
            unauthapi.comics()

    def test_character_by_id(self):
        result = self.api.character(self.wolverine)
        self.assertIsInstance(result, dict)

    def test_character_missing_id(self):
        with self.assertRaises(TypeError):
            self.api.character()

    def test_character_search_for_spiderhypens(self):
        results = self.api.characters(nameStartsWith='Spider-')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_character_search_by_name(self):
        results = self.api.characters(name='3-D Man')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 1)

    def test_characters_comics(self):
        results = self.api.characters_comics(self.doop)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_characters_events(self):
        results = self.api.characters_events(self.doop)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_characters_series(self):
        results = self.api.characters_series(self.doop)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_characters_stories(self):
        results = self.api.characters_stories(self.doop)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_story_by_id(self):
        result = self.api.story(3)
        self.assertIsInstance(result, dict)

    def test_story_missing_id(self):
        with self.assertRaises(TypeError):
            self.api.story()

    def test_stories_with_characters(self):
        results = self.api.stories(characters=[self.wolverine, self.doop])
        self.assertEqual(len(results), results._meta['data']['count'])

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

    def test_creator_by_id(self):
        result = self.api.creator(self.bendis)
        self.assertIsInstance(result, dict)

    def test_creators_comics(self):
        results = self.api.creators_comics(self.bendis)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_creators_events(self):
        results = self.api.creators_events(self.bendis)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_creators_series(self):
        results = self.api.creators_series(self.bendis)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_creators_stories(self):
        results = self.api.creators_stories(self.bendis)
        self.assertEqual(len(results), results._meta['data']['count'])
