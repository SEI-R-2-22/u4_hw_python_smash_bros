import random
import json
from smash import Character, Battle

characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)

def replay():
    input('Do you want to play again? y or n').lower().startswith('y')

def fighter_list():
    for character in characters:
        print(character['name'])

def game():
    print('Welcome to Smash Bros!')
    print('Your choice of fighters are:')
    fighter_list()
    player_choice = input('Choose your warrior! or leave blank for random')
    for character in characters:
        if player_choice == character['name']:
            char1 = character
            print('You chose ' + char1['name'])
        else:
            char1 = random.choice(characters)
            print('Fate has chosen for you ' + char1['name'])





game()