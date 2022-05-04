import random
import json
from smash import Character
from smash import Battle
characters = []

def start_game():
    print('Select a fighter! Character1 or Character2')
    print('Charachter1')
    print('Character2')

    if answer.lower() == 'Character1':
        print('Very Well. Fight!')

    elif answer.lower() == 'Character2':
        print('Hmm, nice choice. Now Brawl!')

with open('characters.json') as json_file:
    characters = json.load(json_file)
