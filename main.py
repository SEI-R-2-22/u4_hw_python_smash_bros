from smash import Battle, Character
import random
import json
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def find_character(name):
    for character in characters:
        if name == character["name"]:
            return character
    return random.choice(characters)


def game():
    character = input("Select your character: ")
    if not character:
        player_character = random.choice(characters)

    player_character = find_character(character)
    print("Your character is " + player_character)

    enemy_character = random.choice(characters)

    player = Character(
        player_character["name"], player_character["attacks"], 100)
    enemy = Character(enemy_character["name"], enemy_character["attacks"], 100)
    fight = Battle(player, enemy)
    fight.battle_start()


game()
