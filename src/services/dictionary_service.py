import os
import random
import sys

from lxml import etree


class Item:
    def __init__(self, string):
        self.word = string[0].text.strip()
        self.definitions = []
        for defn in string[1:]:
            self.definitions.append(defn.text.strip())

    def get_word(self):
        return self.word

    def get_definitions(self):
        return self.definitions


class DictionaryService:
    def __init__(self):
        self.dictionary = self.find_dictionary()
        self.player_dictionary = self.find_player_dictionary()

    def find_dictionary(self):
        source_path = os.path.dirname(__file__)
        dict_path = os.path.join(source_path, "..", "..", "data/dictionary.xml")
        if not os.path.isfile(dict_path):
            print("No dictionary.xml found!")
            sys.exit()
        with open(dict_path, "r") as xml:
            tree = etree.parse(xml)
        return tree.getroot()

    def find_player_dictionary(self):
        source_path = os.path.dirname(__file__)
        dict_path = os.path.join(source_path, "..", "..", "data/player_dictionary.xml")
        if not os.path.isfile(dict_path):
            print("No player_dictionary.xml found!")
            sys.exit()
        with open(dict_path, "r") as xml:
            tree = etree.parse(xml)
        return tree.getroot()

    def add_to_player_dictionary(self, word: str, definitions_as_string: str):
        definitions = definitions_as_string.split("\n")
        definitions = [defn for defn in definitions if defn]  # removes empty lines
        print(definitions)
        # TODO: add word and definitions into player_dictionary.xml

    def get_random_item(self, excluded: list = []):
        if len(excluded) == len(self.dictionary):
            return False
        while True:
            item = Item(self.dictionary[random.randint(0, len(self.dictionary) - 1)])
            if item not in excluded:
                break
        return item


dictionary_service = DictionaryService()
