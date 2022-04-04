import requests
from lxml import etree
import random
import time

lines = []
with open("./sanat.txt", "r") as f:
    for line in f.readlines():
        lines.append(line)


random.shuffle(lines)
lines = lines[:500]
lines.sort()

root = etree.Element("root")

for line in lines:
    res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{line}", timeout=4)
    item = etree.SubElement(root, "item")
    word = etree.SubElement(item, "word")
    try:
        word.text = res.json()[0]["word"]
    except KeyError:  # no definition found, probably
        word.text = str(res.json())
        continue
    for dict in res.json()[0]["meanings"][0]["definitions"]:
        if line.strip() in dict["definition"]:
            continue
        defn = etree.SubElement(item, "defn")
        defn.text = dict["definition"]
    time.sleep(0.05)

et = etree.ElementTree(root)
et.write("sanakirja.xml", pretty_print=True)
