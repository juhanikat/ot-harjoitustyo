import os
import random
from pathlib import Path

from lxml import etree


class Dictionary:
    def __init__(self) -> None:
        source_path = Path(__file__).resolve()
        source_dir = source_path.parent
        dict_path = source_dir.joinpath("dictionary.xml")
        if not os.path.isfile(dict_path):
            print("No dictionary.xml found!")
            exit()
        with open(dict_path, "r") as xml:
            tree = etree.parse(xml)
        self.dictionary = tree.getroot()
        self.dictionary_length = len(self.dictionary)

    def get_random_item(self, excluded: list = None):
        if len(excluded) == self.dictionary_length:
            return False
        while True:
            item = self.dictionary[random.randint(0, len(self.dictionary) - 1)]
            if item not in excluded:
                break
        return item

    def get_readable_word(self, item):
        return item[0].text.strip()

    def get_readable_definitions(self, item):
        result = ""
        i = 1
        for defn in item[1:8]:
            result += f"{i}. {defn.text}\n"
            i += 1
        return result
