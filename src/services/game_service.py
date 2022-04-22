import random

from services.dictionary_service import Item, dictionary_service


class GameService:
    def __init__(self) -> None:
        self.total_points = 0
        self.points_to_gain = 0
        self.attempts = 0
        self.current_item: Item = None
        self.underscores = None
        self.places = None

        self.new_item()

    def new_item(self):
        self.current_item = dictionary_service.get_random_item()
        word = self.current_item.get_word()
        self.places = list(range(len(word)))
        random.shuffle(self.places)
        # reset underscores and points to gain
        self.underscores = ["_" for _ in range(len(word))]
        self.points_to_gain = 10
        return self.current_item

    def reveal_next_letter(self):
        if len(self.places) > 0:
            index = self.places.pop()
            self.underscores[index] = self.current_item.get_word()[index]
            if self.points_to_gain > 0:
                self.points_to_gain -= 1

    def get_readable_underscores(self):
        return " ".join(self.underscores)

    def get_word_length(self):
        if self.current_item:
            return len(self.current_item.get_word())
        return False

    def get_total_points(self):
        return self.total_points

    def get_points_to_gain(self):
        return self.points_to_gain

    def check_answer(self, answer):
        """Returns True and adds points if the answer was correct, and returns False otherwise."""
        if self.current_item:
            if answer.strip() == self.current_item.get_word():
                self.total_points += self.points_to_gain
                return True
        return False

    def get_readable_definitions(self):
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
