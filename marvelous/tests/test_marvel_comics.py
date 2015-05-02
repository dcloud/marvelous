from marvelous.tests.base import MarvelTests


class TestMarvelComics(MarvelTests):

    def test_comic_by_id(self):
        result = self.api.comic(self.ultron_comic)
        self.assertIsInstance(result, dict)

    def test_comics_characters(self):
        results = self.api.comics_characters(self.ultron_comic)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_comics_creators(self):
        results = self.api.comics_creators(self.ultron_comic)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_comics_events(self):
        results = self.api.comics_events(self.ultron_comic)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_comics_stories(self):
        results = self.api.comics_stories(self.ultron_comic)
        self.assertEqual(len(results), results._meta['data']['count'])
