from marvelous.tests.base import MarvelTests


class TestMarvelCharacters(MarvelTests):

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
