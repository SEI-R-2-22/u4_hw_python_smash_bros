import random
import json
from smash import Character, Battle

characters = []

player = {}
enemy = {}

with open('characters.json') as json_file:
    characters = json.load(json_file)


def find_character(name):
    for character in characters:
        if name == character["name"]:
            return character
    return None


def game():
    selected = input('Choose your Character: ')
    if not selected:
        selected = random.choice(characters)
    print('You have chosen ' + selected)
    player = find_character(selected)

    enemy = random.choice(characters)

    current_player = Character(player["name"], 60, player["attacks"])
    computer = Character(enemy["name"], 60, enemy["attacks"])

    new_game = Battle(current_player, computer)
    new_game.fight()


game()
