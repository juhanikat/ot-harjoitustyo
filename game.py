from lxml import etree
import random


def main():
    with open("./sanakirja.xml") as xml:
        tree = etree.parse(xml)
        
    dictionary = tree.getroot()
    while True:
        item = dictionary[random.randint(0, len(dictionary) - 1)]
        word = item[0].text.strip()
        print('----------------')
        for category in item[1]:
            print(f"{category.tag.capitalize()}:")
            for defn in category:
                print(defn.text)
        print('----------------')
        while True:
            answer = input("(Input q to quit) The word is: ").strip().lower()
            if answer == "q":
                return
            if answer == word:
                print(f"Correct! The word was {word}.")
                break
            else:
                print("Nope, try again.")
if __name__ == '__main__':
    main()
