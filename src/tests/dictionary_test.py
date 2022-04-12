import unittest

from services.dictionary_service import dictionary_service
from services.game_service import game_service


class TestGame(unittest.TestCase):
    def setUp(self):
        self.item = game_service.new_item()

    def test_get_readable_word_returns_string(self):
        word = self.item.get_word()
        self.assertIsInstance(word, str)

    def test_check_answer_return_correct_truth_value(self):
        word = self.item.get_word()
        result = game_service.check_answer(word)
        self.assertEqual(result, True)
        result = game_service.check_answer("asdasdasdasdasd")
        self.assertEqual(result, False)
