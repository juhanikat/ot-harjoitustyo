from lxml import etree
import os
import random

class Dictionary:

    def __init__(self) -> None:
        if not os.path.isfile('dictionary.xml'):
            print("No dictionary.xml found!")
            exit()
        with open('dictionary.xml', 'r') as xml:
            tree = etree.parse(xml)
            self.dictionary = tree.getroot()

    def get_random_item(self):
        item = self.dictionary[random.randint(0, len(self.dictionary) - 1)]
        return item

    def get_readable_word(self, item):
        return item[0].text.strip()
    
    def get_readable_definitions(self, item):
        result = ""
        for category in item[1]:
            result+=f"{category.tag.capitalize()}:\n"
            i = 1
            for defn in category:
                result+=f"{i}. {defn.text}\n"
                i+= 1
        return result

