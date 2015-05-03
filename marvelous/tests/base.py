import unittest
import os

from marvelous.marvel import Marvel

MARVEL_API_PUBLIC_KEY = os.environ.get('MARVEL_API_PUBLIC_KEY', '')
MARVEL_API_PRIVATE_KEY = os.environ.get('MARVEL_API_PRIVATE_KEY', '')


class MarvelTests(unittest.TestCase):

    def setUp(self):
        self.api = Marvel(public_key=MARVEL_API_PUBLIC_KEY, private_key=MARVEL_API_PRIVATE_KEY)
        self.wolverine = 1009718
        self.doop = 1009279
        self.bendis = 24
        self.story = 15
        self.ultron_comic = 45908
        self.age_of_ultron_event = 314
        self.avengers_series = 1991
