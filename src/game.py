import dictionary
import random


class Game:

    def __init__(self) -> None:
        self.d = dictionary.Dictionary()
        self.points = 0
        self.attempts = 0

    def reveal_next_letter(self, original_word, revealed_word):
        while True:
            index = random.randint(0,len(original_word)-1)
            if revealed_word[index] == '_':
                break
        revealed_word = list(revealed_word)
        revealed_word[index] = original_word[index]
        revealed_word = ''.join(revealed_word)
        return revealed_word
    
    def playing_loop(self):
        seen = []
        while True:
            item = self.d.get_random_item(excluded=seen)
            if item == False:
                print()
                print("You got through every word in the dictionary, congrats!")
                self.end_game()
            seen.append(item)
            word = self.d.get_readable_word(item)
            revealed_word = ''.join(['_'] * len(word))
            print()
            print('----------------')
            print(f"Guess the following {len(word)} letter word: ")
            print(self.d.get_readable_definitions(item))
            while True:
                print("(Input q to quit, s to skip, or hint to reveal a letter)")
                answer = input("The word is: ").strip().lower()
                if answer == "q":
                    self.end_game()
                elif answer == 's':
                    break
                elif answer == 'hint':
                    revealed_word = self.reveal_next_letter(word, revealed_word)
                    if not "_" in revealed_word:
                         print(f"The word was {word}.")
                         break
                    else:
                        print(revealed_word)
                elif answer == word:
                    print(f"Correct! The word was {word}.")
                    self.points += 1
                    print(f"Points: {self.points}")
                    break
                else:
                    print("Nope, try again.")

    def end_game(self):
        print(f'Final score: {self.points} points')
        exit()
    
if __name__ == '__main__':
    game = Game()
    game.playing_loop()
