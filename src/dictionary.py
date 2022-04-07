import os
import random
import sys
from pathlib import Path

from lxml import etree


class Item:
    def __init__(self, string) -> None:
        self.word = string[0].text.strip()
        self.definitions = []
        for defn in string[1:]:
            self.definitions.append(defn.text)

    def get_readable_word(self):
        return self.word

    def get_readable_definitions(self):
        result = ""
        i = 1
        for defn in self.definitions:
            result += f"{i}. {defn}\n"
            i += 1
        return result


class Dictionary:
    def __init__(self) -> None:
        source_path = Path(__file__).resolve()
        source_dir = source_path.parent
        dict_path = source_dir.joinpath("dictionary.xml")
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
