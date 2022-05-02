import random
import json
from smash import Battle, Character

characters = []

player_character = {}
enemy_character = {}

with open('characters.json') as json_file:
    characters = json.load(json_file)


def find_character(name):
    for character in characters:
        if name == character["name"]:
            return character
    return None


def game():
    character = input("Select your character: ")
    if not character:
        character = random.choice(characters)
    print("Your character is " + character)
    player_character = find_character(character)

    enemy = random.choice(characters)

    player = Character(
        player_character["name"], 60, player_character["attacks"])
    computer = Character(enemy["name"], 60, enemy["attacks"])

    new_game = Battle(player, computer)
    new_game.battling()


game()
