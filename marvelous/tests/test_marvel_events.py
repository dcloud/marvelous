from marvelous.tests.base import MarvelTests


class TestMarvelEvents(MarvelTests):

    def test_event_by_id(self):
        result = self.api.event(self.age_of_ultron_event)
        self.assertIsInstance(result, dict)

    def test_event_missing_id(self):
        with self.assertRaises(TypeError):
            self.api.event()

    def test_events_characters(self):
        results = self.api.events_characters(self.age_of_ultron_event)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_events_comics(self):
        results = self.api.events_comics(self.age_of_ultron_event)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_events_creators(self):
        results = self.api.events_creators(self.age_of_ultron_event)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_events_series(self):
        results = self.api.events_series(self.age_of_ultron_event)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])

    def test_events_stories(self):
        results = self.api.events_stories(self.age_of_ultron_event)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), results._meta['data']['count'])
