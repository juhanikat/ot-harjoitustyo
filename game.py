from lxml import etree
import random

with open("./sanakirja.xml") as xml:
    tree = etree.parse(xml)
    dictionary = tree.getroot()
    rnd = dictionary[random.randint(0, len(dictionary)-1)]
    word = rnd[0].text.strip()
    print()
    for defn in rnd[1]:
        print(defn.text)
    print()
    while True:
        answer = input("(Input q to quit) The word is: ").strip().lower()
        if answer == 'q':
            break
        if answer == word:
            print("Correct!")
            break
        else:
            print("Nope")