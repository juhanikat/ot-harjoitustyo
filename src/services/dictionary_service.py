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

    def get_readable_word(self):
        return self.word

    def get_readable_definitions(self):
        result = ""
        i = 1
        for defn in self.definitions:
            result += f"{i}. {defn}"
            i += 1
        return result


class DictionaryService:
    def __init__(self):
        source_path = os.path.dirname(__file__)
        dict_path = os.path.join(source_path, "..", "..", "data/dictionary.xml")
        if not os.path.isfile(dict_path):
            print("No dictionary.xml found!")
            sys.exit()
        with open(dict_path, "r") as xml:
            tree = etree.parse(xml)
        self.dictionary = tree.getroot()
        self.dictionary_length = len(self.dictionary)

    def get_random_item(self, excluded: list = []):
        if len(excluded) == self.dictionary_length:
            return False
        while True:
            item = Item(self.dictionary[random.randint(0, len(self.dictionary) - 1)])
            if item not in excluded:
                break
        return item


dictionary_service = DictionaryService()
