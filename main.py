from smash import Battle, Character
import random
import json

characters = []
restart = 'Y'

with open('characters.json') as json_file:
    characters = json.load(json_file)

def character_selector(smash_char_name):

    for character in characters:
        if smash_char_name.lower() == character["name"].lower():
            return character
    return None

def new_game():

    smash_char_name = input("Enter character name: ")
    character = character_selector(smash_char_name)
    player_one = Character(character["name"], 100, character["attacks"])
    if not smash_char_name or character is None:
        character = random.choice(characters)

    cpu_enemy = random.choice(characters)
    player_two = Character(cpu_enemy["name"], 100, cpu_enemy["attacks"])

    print("Player One has chosen: " + player_one.name)
    print("Player Two has chosen: " + player_two.name)
    print("Let the game begin")
    print("------------------------------------------")

    game_reset = Battle(player_one, player_two)
    game_reset.fighting()

while restart == 'Y':
    new_game()
    restart = input("Game Over. Would you like a rematch? (Type 'Y' for Yes or 'N' for No) ")

print("Game turning off...")