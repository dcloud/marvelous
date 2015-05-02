import unittest
import os

from marvelous.marvel import Marvel
from marvelous.exceptions import APIError

MARVEL_API_PUBLIC_KEY = os.environ.get('MARVEL_API_PUBLIC_KEY', '')
MARVEL_API_PRIVATE_KEY = os.environ.get('MARVEL_API_PRIVATE_KEY', '')


class TestMarvel(unittest.TestCase):

    def setUp(self):
        self.api = Marvel(public_key=MARVEL_API_PUBLIC_KEY, private_key=MARVEL_API_PRIVATE_KEY)

    def test_needs_public_and_private_keys(self):
        unauthapi = Marvel()
        with self.assertRaises(APIError):
            unauthapi.comics()

    def test_character_by_id(self):
        result = self.api.character(1011334)
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

    def test_story_by_id(self):
        result = self.api.story(3)
        self.assertIsInstance(result, dict)

    def test_story_missing_id(self):
        with self.assertRaises(TypeError):
            self.api.story()