import random
import json
from smash import Character, Battle
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def game():
    print('Please select your character!(1/2)')
    if input == '1':
        print("Great, you are player 1")
    else:
        print('Great, you are player 2')
