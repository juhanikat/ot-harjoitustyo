import unittest

import dictionary


class TestGame(unittest.TestCase):
    def setUp(self):
        self.d = dictionary.Dictionary()

    def test_dictionary_is_created(self):
        self.assertIsInstance(self.d, dictionary.Dictionary)

    def test_get_readable_word_returns_string(self):
        word = self.d.get_random_item().get_readable_word()
        self.assertIsInstance(word, str)
