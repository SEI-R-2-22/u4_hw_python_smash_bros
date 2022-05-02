import random
import json
from smash import Battle, Character

characters = []

player_character = {}
opponent = {}

with open('characters.json') as json_file:
    characters = json.load(json_file)


def find_character(name):
    for character in characters:
        if name == character["name"]:
            return character
    return None


def game():
    character = input(
        'Type a chracter name, if you do not select a name a random one will be found ')
    if not character:
        character = random.choice(characters)["name"]
        # character = find_character(selected_character)
    print("CHARACTER:" + character)
    player_character = find_character(character)

    opponent = random.choice(characters)

    user = Character(player_character["name"], 50, player_character["attacks"])
    computer = Character(opponent["name"], 50, opponent["attacks"])

    # print(user.moves)
    new_game = Battle(user, computer)
    new_game.fight()


game()
