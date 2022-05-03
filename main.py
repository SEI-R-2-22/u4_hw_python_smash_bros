import random
import json
from unicodedata import name
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def choose_characters():
    print("please choose a player ")
    str(input(characters))
   




choose_characters()