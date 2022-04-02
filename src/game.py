import dictionary



class Game:

    def __init__(self) -> None:
        self.d = dictionary.Dictionary()
        self.points = 0
    
    def playing_loop(self):
        while True:
            item = self.d.get_random_item()
            word = self.d.get_readable_word(item)
            print()
            print('----------------')
            print(f"Guess the following word: {' '.join(['_'] * len(word))}")
            print(self.d.get_readable_definitions(item))
            print('----------------') 
            while True:
                answer = input("(Input q to quit) The word is: ").strip().lower()
                if answer == "q":
                    print(f"Final score: {self.points} points")
                    return
                if answer == word:
                    print(f"Correct! The word was {word}.")
                    self.points += 1
                    print(f"Points: {self.points}")
                    break
                else:
                    print("Nope, try again.")
    
if __name__ == '__main__':
    game = Game()
    game.playing_loop()
