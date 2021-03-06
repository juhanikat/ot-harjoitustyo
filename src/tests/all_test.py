import unittest
import os
from pathlib import Path

from services.dictionary_service import (
    dictionary_service,
    InvalidCategoryError,
    EmptyItemError,
)
from services.game_service import game_service

root_dir = Path(__file__).parents[2]


class TestGame(unittest.TestCase):
    def setUp(self):
        self.item = game_service.new_item(category="main")

    def test_starting_program_creates_player_dictionary_file(self):
        self.assertTrue(
            os.path.isfile(os.path.join(root_dir, "data/player_dictionary.xml"))
        )

    def test_get_readable_word_returns_string(self):
        word = self.item.get_word()
        self.assertIsInstance(word, str)

    def test_check_answer_return_correct_truth_value(self):
        word = self.item.get_word()
        result = game_service.check_answer(word)
        self.assertEqual(result, True)
        result = game_service.check_answer("asdasd")
        self.assertEqual(result, False)

    def test_reveal_next_letter_decreases_points(self):
        self.assertEqual(game_service.get_points_to_gain(), 10)
        game_service.reveal_next_letter()
        self.assertEqual(game_service.get_points_to_gain(), 9)

    def test_new_item_resets_points_to_gain(self):
        game_service.reveal_next_letter()
        self.assertEqual(game_service.get_points_to_gain(), 9)
        game_service.new_item(category="main")
        self.assertEqual(game_service.get_points_to_gain(), 10)

    def test_points_to_gain_stays_positive(self):
        for _ in range(30):
            game_service.reveal_next_letter()
        self.assertGreaterEqual(game_service.get_points_to_gain(), 0)

    def test_getting_new_item_from_different_categories(self):
        game_service.new_item(category="main")
        game_service.new_item(category="custom")
        self.assertRaises(
            InvalidCategoryError, game_service.new_item, category="asdasd"
        )

    def test_add_empty_item_to_player_dictionary(self):
        self.assertRaises(
            EmptyItemError, dictionary_service.add_to_player_dictionary, "", ""
        )
        self.assertRaises(
            EmptyItemError, dictionary_service.add_to_player_dictionary, " ", " "
        )
        self.assertRaises(
            EmptyItemError, dictionary_service.add_to_player_dictionary, "", "asdasd"
        )
        self.assertRaises(
            EmptyItemError, dictionary_service.add_to_player_dictionary, "asdasd", ""
        )
