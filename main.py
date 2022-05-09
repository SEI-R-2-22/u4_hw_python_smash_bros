import random
import json
from smash import Character, Battle

characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


player_choice = input('Choose your character: ')

for character in characters:
    if player_choice.lower() == character["name"].lower():
        player_character = Character(character["name"], character["attacks"])

comp_choice = random.choice(characters)
comp_character = Character(comp_choice["name"], comp_choice["attacks"])


def dual():
    battle = Battle(player_character, comp_character)
    while battle.character1.health > 0 and battle.character2.health > 0:
        comp_character.decrement_health(
            player_character.random_attack()["damage"])
        player_character.decrement_health(
            comp_character.random_attack()["damage"]
        )
