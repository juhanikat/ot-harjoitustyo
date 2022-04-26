import os
import random
import sys

from lxml import etree

source_path = os.path.dirname(__file__)


class Item:
    def __init__(self, string):
        self.word = string[0].text.strip()
        self.definitions = []
        for defn in string[1:]:
            self.definitions.append(defn.text.strip())

    def get_word(self) -> list:
        return self.word

    def get_definitions(self) -> list:
        return self.definitions


class DictionaryService:
    def __init__(self):
        self.dictionary = self.get_dictionary()
        self.player_dictionary = self.get_player_dictionary()

    def get_dictionary(self):
        dict_path = os.path.join(source_path, "..", "..", "data/dictionary.xml")
        if not os.path.isfile(dict_path):
            print("No dictionary.xml found!")
            sys.exit()
        with open(dict_path, "r") as xml:
            tree = etree.parse(xml)
        return tree.getroot()

    def get_player_dictionary(self):
        dict_path = os.path.join(source_path, "..", "..", "data/player_dictionary.xml")
        if not os.path.isfile(dict_path):
            print("No player_dictionary.xml found!")
            sys.exit()
        with open(dict_path, "r") as xml:
            tree = etree.parse(xml)
        return tree.getroot()

    def add_to_player_dictionary(self, word: str, definitions_as_string: str) -> None:
        if len(word) == 0 or len(definitions_as_string) == 0:
            print("No empty words")
            return
        self.player_dictionary = self.get_player_dictionary()
        definitions = definitions_as_string.split("\n")
        definitions = [defn for defn in definitions if defn]  # removes empty lines

        # TODO: add word and definitions into player_dictionary.xml
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

    def get_random_item(self, excluded: list = []) -> Item:
        if len(excluded) == len(self.dictionary):
            return False
        while True:
            item = Item(self.dictionary[random.randint(0, len(self.dictionary) - 1)])
            if item not in excluded:
                break
        return item


dictionary_service = DictionaryService()
