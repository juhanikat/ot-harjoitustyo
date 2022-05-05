import os
import random
import sys

from entities.item import Item
from lxml import etree

source_path = os.path.dirname(__file__)


class InvalidCategoryError(Exception):
    pass


class EmptyItemError(Exception):
    pass


class NoDictError(Exception):
    pass


class DictionaryService:
    """Handles getting data from the xml files and adding data to player_dictionay.xml.

    Attributes:
        dictionary: The root element of dictionary.xml.
        player_dictionary: the root element of player_dictionary.xml.
    """

    def __init__(self):
        try:
            self.dictionary = self.get_dictionary_root()
        except NoDictError as error:
            print(error)
            sys.exit()
        self.player_dictionary = self.get_player_dictionary_root()
        self.player_dict_is_empty = False

    def get_dictionary_root(self):
        """
        Returns:
            The root element of the dictionary.xml file.
        """
        dict_path = os.path.join(source_path, "..", "..", "data/dictionary.xml")
        if not os.path.isfile(dict_path):
            raise NoDictError("No dictionary.xml found!")
        with open(dict_path, "r") as xml:
            tree = etree.parse(xml)
        return tree.getroot()

    def get_player_dictionary_root(self):
        """
        Returns:
            The root element of the player_dictionary.xml file.
        """
        dict_path = os.path.join(source_path, "..", "..", "data/player_dictionary.xml")
        if not os.path.isfile(dict_path) or os.path.getsize(dict_path) == 0:
            self.player_dict_is_empty = True
            with open(dict_path, "w") as file:  # creates the file and adds root tag
                file.write(
                    "<root><item><word>placeholder</word><defn>you don't have any custom words, add some using the 'Add Custom Words' button.</defn></item></root>"
                )
            return False
        with open(dict_path, "r") as xml:
            tree = etree.parse(xml)
        return tree.getroot()

    def add_to_player_dictionary(self, word: str, definitions_as_string: str) -> None:
        """Adds a custom word and its definitions as an element into the player_dictionary.xml file.

        Args:
            word (str): The custom word.
            definitions_as_string (str): The custom word's definitions.
        """
        word, definitions_as_string = word.strip(), definitions_as_string.strip()
        if len(word) == 0 or len(definitions_as_string) == 0:
            raise EmptyItemError("The word or its definitions can not be empty.")
        self.player_dict_is_empty = False
        self.player_dictionary = self.get_player_dictionary_root()
        definitions = definitions_as_string.split("\n")
        definitions = [
            defn.strip() for defn in definitions if defn
        ]  # removes empty lines

        item = etree.SubElement(self.player_dictionary, "item")
        word_tag = etree.SubElement(item, "word")
        word_tag.text = word
        for defn in definitions:
            defn_tag = etree.SubElement(item, "defn")
            defn_tag.text = defn
        dict_path = os.path.join(source_path, "..", "..", "data/player_dictionary.xml")
        self.player_dictionary.append(item)
        tree = etree.ElementTree(self.player_dictionary)
        tree.write(dict_path, pretty_print=True)

    def get_random_item(self, *, category) -> Item:
        """Return a random item from dictionary.xml or player_dictionary.xml.

        Args:
            category: If "main", the item is selected from dictionary.xml. If "custom", the item is selected from player_dictionary.xml.

        Raises:
            InvalidCategoryError: Raised if category is not "main" nor "custom".

        Returns:
            Item: A random <item> element from dictionary.xml or player_dictionary.xml.
        """
        if category == "custom":
            if self.player_dict_is_empty:
                return False
            dictio = self.get_player_dictionary_root()
        elif category == "main":
            dictio = self.dictionary
        else:
            raise InvalidCategoryError("Invalid category name!")
        item = Item(dictio[random.randint(0, len(dictio) - 1)])
        return item


dictionary_service = DictionaryService()
