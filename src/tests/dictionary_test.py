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

    def test_reveal_next_letter_decreases_points(self):
        self.assertEqual(game_service.get_points_to_gain(), 10)
        game_service.reveal_next_letter()
        self.assertEqual(game_service.get_points_to_gain(), 9)

    def test_new_item_resets_points_to_gain(self):
        game_service.reveal_next_letter()
        self.assertEqual(game_service.get_points_to_gain(), 9)
        game_service.new_item()
        self.assertEqual(game_service.get_points_to_gain(), 10)

    def test_points_to_gain_stays_positive(self):
        for _ in range(20):
            game_service.reveal_next_letter()
        self.assertGreaterEqual(game_service.get_points_to_gain(), 0)
