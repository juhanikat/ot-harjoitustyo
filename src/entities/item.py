class Item:
    """Represents a dictionary item.

    Attributes:
        word: The word.
        definitions: The word's definitions.
    """

    def __init__(self, string):
        self.word = string[0].text.strip()
        self.definitions = []
        for defn in string[1:]:
            self.definitions.append(defn.text.strip())

    def get_word(self) -> str:
        """Returns word as a string."""
        return self.word

    def get_definitions(self) -> list:
        """Returns definitions as a list."""
        return self.definitions
