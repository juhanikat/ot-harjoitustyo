import random

from entities.item import Item

from services.dictionary_service import dictionary_service


class GameService:
    """Handles the game mechanics.

    Attributes:
        total_points: The amount of points gained so far.
        points_to_gain: The amount of points that can be gained from guessing the current word.
        attempts: The amount of attempts the player has made so far.
        current_item: The current word and its definitions.
        underscores: A list of underscores that can be replaced with letters from the current word.

    """

    def __init__(self) -> None:
        self.total_points = 0
        self.points_to_gain = 0
        self.attempts = 0
        self.current_item: Item = None
        self.underscores = None
        self.places = None

        self.new_item(category="main")

    def new_item(self, *, category) -> Item:
        """Chooses a new word and resets hints and points to gain.

        Args:
            category: Determines if the new word is a custom word ("custom"), or a default one ("main").

        Returns:
            Item: The new word and its definitions.
        """
        new_item = dictionary_service.get_random_item(category=category)
        if not new_item:
            return False
        self.current_item = new_item
        word = self.current_item.get_word()
        self.places = list(range(len(word)))
        random.shuffle(self.places)
        # reset underscores and points to gain
        self.underscores = ["_" for _ in range(len(word))]
        self.points_to_gain = 10
        self.attempts = 0
        return self.current_item

    def decrease_points_to_gain(self, amount):
        if self.points_to_gain >= amount:
            self.points_to_gain -= amount

    def reveal_next_letter(self):
        if len(self.places) > 0:
            index = self.places.pop()
            self.underscores[index] = self.current_item.get_word()[index]
            self.decrease_points_to_gain(1)

    def get_readable_underscores(self):
        """Returns underscores as a string."""
        return " ".join(self.underscores)

    def get_word_length(self):
        """Returns the length of the current word if it exists, and False otherwise."""
        if self.current_item:
            return len(self.current_item.get_word())
        return False

    def get_total_points(self):
        """Returns total points."""
        return self.total_points

    def get_attempts(self):
        return self.attempts

    def increase_attempts(self):
        self.attempts += 1

    def get_points_to_gain(self):
        """Returns points that can be gained from guessing the current word."""
        return self.points_to_gain

    def check_answer(self, answer: str):
        """Returns True and adds points if the answer was correct, and False otherwise."""
        if self.current_item:
            self.increase_attempts()
            if answer.strip() == self.current_item.get_word():
                self.total_points += self.points_to_gain
                return True
            self.decrease_points_to_gain(1)
        return False

    def get_readable_definitions(self) -> list:
        """Returns a list of definitions for the current word."""
        if self.current_item:
            result = []
            i = 1
            for defn in self.current_item.get_definitions():
                result.append(f"{i}. {defn}\n")
                i += 1
            return result
        return False


game_service = GameService()
