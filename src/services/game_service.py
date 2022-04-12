import random
import sys

from services.dictionary_service import Item, dictionary_service


class GameService:
    def __init__(self) -> None:
        self.points = 0
        self.attempts = 0
        self.current_item: Item = None
        self.underscores = None
        self.places = None

        self.new_item()

    def new_item(self):
        self.current_item = dictionary_service.get_random_item()
        word = self.current_item.get_word()
        self.underscores = ["_" for _ in range(len(word))]
        self.places = list(range(len(word)))
        random.shuffle(self.places)
        return self.current_item

    def reveal_next_letter(self):
        if len(self.places) > 0:
            index = self.places.pop()
            self.underscores[index] = self.current_item.get_word()[index]

    def get_readable_underscores(self):
        return " ".join(self.underscores)

    def get_word_length(self):
        if self.current_item:
            return len(self.current_item.get_word())
        return False

    def check_answer(self, answer):
        if self.current_item:
            if answer.strip() == self.current_item.get_word():
                return True
            return False
        return False

    def get_readable_definitions(self):
        if self.current_item:
            result = []
            i = 1
            for defn in self.current_item.get_definitions():
                result.append(f"{i}. {defn}\n")
                i += 1
            return result
        return False

    def end_game(self):
        print(f"Final score: {self.points} points")
        sys.exit()


game_service = GameService()
