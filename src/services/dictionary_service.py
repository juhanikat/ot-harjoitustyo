import os
import random
import sys

from entities.item import Item
from lxml import etree

source_path = os.path.dirname(__file__)


class InvalidCategoryError(Exception):
    """Raised if get_random_item() gets an invalid category name in its "category" parameter."""


class EmptyItemError(Exception):
    """Raised if player tries to add an empty item to the dictionary."""


class NoDictError(Exception):
    """Raised if dictionary.xml does not exist."""


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

    def get_dictionary_root(self):
        """Raises:
           NoDictError: Raised if dictionary.xml doesn't exist.

        Returns:
           The root element of the dictionary.xml file.
        """
        dict_path = os.path.join(source_path, "..", "..", "data/dictionary.xml")
        if not os.path.isfile(dict_path):
            raise NoDictError("No dictionary.xml found!")
        with open(dict_path, "r", encoding="UTF-8") as xml:
            tree = etree.parse(xml)
        return tree.getroot()

    def get_player_dictionary_root(self):
        """
        Returns:
            The root element of the player_dictionary.xml file, or if file doesn't exist, creates it and returns False.
        """
        dict_path = os.path.join(source_path, "..", "..", "data/player_dictionary.xml")
        if not os.path.isfile(dict_path) or os.path.getsize(dict_path) == 0:
            with open(
                dict_path, "w", encoding="UTF-8"
            ) as file:  # creates the file and adds root tag
                file.write("<root></root>")
            return False
        with open(dict_path, "r", encoding="UTF-8") as xml:
            tree = etree.parse(xml)
        return tree.getroot()

    def add_to_player_dictionary(self, word: str, definitions_as_string: str) -> None:
        """Adds a custom word and its definitions as an element into the player_dictionary.xml file.

        Raises:
            EmptyItemError: Raised if player tries to add an empty item to the dictionary.
        Args:
            word (str): The custom word.
            definitions_as_string (str): The custom word's definitions (each definition
            is separated by a newline).
        """
        word, definitions_as_string = word.strip(), definitions_as_string.strip()
        if len(word) == 0 or len(definitions_as_string) == 0:
            raise EmptyItemError("The word or its definitions can not be empty.")
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
            category: If "main", the item is selected from dictionary.xml. If "custom", the item is
            selected from player_dictionary.xml.

        Raises:
            InvalidCategoryError: Raised if category is not "main" or "custom".

        Returns:
            Item: A random <item> element from dictionary.xml or player_dictionary.xml.
        """
        if category == "custom":
            dictio = self.get_player_dictionary_root()
            if len(dictio) == 0:
                return False
        elif category == "main":
            dictio = self.dictionary
        else:
            raise InvalidCategoryError("Invalid category name!")
        item = Item(dictio[random.randint(0, len(dictio) - 1)])
        return item


dictionary_service = DictionaryService()
