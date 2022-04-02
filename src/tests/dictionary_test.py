import unittest
import dictionary


class TestGame(unittest.TestCase):

    def setUp(self):
        pass

    def test_dictionary_is_created(self):
        d = dictionary.Dictionary()
        self.assertIsInstance(d,dictionary.Dictionary)


