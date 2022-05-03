import random
import json
from smash import Battle, Character

characters = []


with open('characters.json') as json_file:
    characters = json.load(json_file)


def find_character(name):
    for character in characters:
        if name == character["name"]:
            return character
    return None


def game():
    character_name = input("Type a character's name: ")
    character = find_character(character_name)
    player = Character(character["name"], 50, character["attacks"])
    if not character_name or character is None:
        character = random.choice(characters)

        opponent = random.choice(characters)
        enemy = Character(opponent["name"], 70, opoonent['attacks'])

        new_game = Battle(player, enemy)
        new_game.battling()
