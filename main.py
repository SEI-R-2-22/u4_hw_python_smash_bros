import random
import json
from smash import Battle, Character

characters = []
CPU = None
PC = None

with open('characters.json') as json_file:
    characters = json.load(json_file)
