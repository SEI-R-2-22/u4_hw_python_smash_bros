import random
import json
from unicodedata import name
from smash import Battle, Character

characters = []
CPU = None
PC = None


with open('characters.json') as json_file:
    characters = json.load(json_file)


for character in characters:
    print(character["name"])

character_choice = input()
