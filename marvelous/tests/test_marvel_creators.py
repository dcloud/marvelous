from marvelous.tests.base import MarvelTests


class TestMarvelCreators(MarvelTests):

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
