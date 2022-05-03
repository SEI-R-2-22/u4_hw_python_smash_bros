import random
import json
import character

characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)
