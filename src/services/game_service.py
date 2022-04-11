from services.dictionary_service import Dictionary
import random


class GameService:
    def __init__(self) -> None:
        self.dictionary = Dictionary()
        self.points = 0
        self.attempts = 0

        self.current_item = None

    def new_item(self):
        self.current_item = self.dictionary.get_random_item()

    def reveal_next_letter(self, original_word, revealed_word):
        while True:
            index = random.randint(0, len(original_word) - 1)
            if revealed_word[index] == "_":
                break
        revealed_word = list(revealed_word)
        revealed_word[index] = original_word[index]
        revealed_word = "".join(revealed_word)
        return revealed_word

    def get_word_length(self):
        return len(self.current_item.word)

    def check_answer(self, answer):
        if answer == self.current_item.word:
            return True
        return False

    def get_readable_definitions(self):
        result = []
        i = 1
        for defn in self.current_item.definitions:
            result.append(f"{i}. {defn}\n")
            i += 1
        return result

    def new_word_loop(self):
        seen = []
        while True:
            item = self.words.get_random_item(excluded=seen)
            if item is False:
                print()
                print("You got through every word in the dictionary, congrats!")
                self.end_game()
            seen.append(item)
            word = item.get_readable_word()
            print()
            print("----------------------")
            print(f"Guess this {len(word)} letter word: ")
            print(item.get_readable_definitions())
            self.answer_loop(word)

    def answer_loop(self, word):
        revealed_word = "".join(["_"] * len(word))
        while True:
            print("(Input q to quit, s to skip, or h to reveal a letter)")
            answer = input("The word is: ")
            answer = answer.strip().lower()
            if answer == "q":
                self.end_game()
            elif answer == "s":
                return
            elif answer == "h":
                revealed_word = self.reveal_next_letter(word, revealed_word)
                if "_" not in revealed_word:
                    print()
                    print(f"The word was {word}.")
                    return
                print(" ".join(revealed_word))
            elif answer == word:
                print()
                print(f"Correct! The word was {word}.")
                self.points += 1
                print(f"Points: {self.points}")
                return
            else:
                print("No, try again.")
                self.attempts += 1

    def end_game(self):
        print(f"Final score: {self.points} points")
        sys.exit()


game_service = GameService()
