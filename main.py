import random
import json
from smash import Character, Battle

characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def obtain_character(character_name):
    for character in characters:
        if character_name.lower() == character["name"].lower():
            return character
    return None


def game():
    character_name = input("Type a character's name: ")
    character = obtain_character(character_name)
    if not character_name or character is None:
        character = random.choice(characters)

    computer = random.choice(characters)

    player = Character(character["name"], character["attacks"])

    competition = Character(computer["name"], computer["attacks"])

    print(character["name"] + " will be facing " + computer["name"])

    battle = Battle(player, competition)
    battle.runit()


def restart():
    choice = input('Would you like to play again? (yes/no)')
    if choice == 'yes':
        game()
    elif choice == 'no':
        print('Thanks for playing!')

    else:
        print('That will not work. Please pick again. (yes/no)')
        restart()


game()
restart()
