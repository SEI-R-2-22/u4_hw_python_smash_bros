from ctypes.wintypes import PCHAR
import random
import json
from unicodedata import name
from smash import Battle, Character

characters = []
CPU = None
PC = None


with open('characters.json') as json_file:
    characters = json.load(json_file)


# choose = input('Ready to fight? (Y/N)')
#     if choose.lower().strip() == 'y':

def fighter_selection():
    # fighters = []
    for character in characters:
        # fighters.append(character["name"])
        print('Pick fighter!')
        print(character["name"])
        # print(fighters)
        character_choice = input().strip()
        if character_choice.lower().strip() in characters:
            if character_choice.lower().strip() == character["name"]:
                PC = Character(character['name'], character['attacks'])
                print("You picked- " + PC.name)
                break
        else:
            print("Invalid choice! Choose fighter from list.")
            fighter_selection()

# def choose_fighter(name):
#     for character in characters:
#         print(character["name"])


def game():
    fighter_selection()


game()
