import random
import json
from smash import Character, Battle

characters = []
char_names = []
player_char = {}
nme_char = {}

with open('characters.json') as json_file:
    characters = json.load(json_file)


def game():
    for character in characters:
        print(character["name"])
        char_names.append(character["name"])
    chooseChar = input('Choose your character: ')
    if chooseChar in char_names:
        for character in characters:
            if chooseChar == character["name"]:
                player_char = character
                print('You choose: ' + str(character["name"]))
            else:
                None
    else:
        player_char = random.choice(characters)
        print('Invalid choice, ' +
              str(player_char["name"]) + ' has been chosen for you.')
    print('Player Char', player_char)
    nme_char = random.choice(characters)
    print('Your opponent is: ' + nme_char["name"])
    print('NME Char', nme_char)

    player = Character(player_char["name"], 50, player_char["attacks"])
    computer = Character(nme_char["name"], 50, nme_char["attacks"])

    new_game = Battle(player, computer)
    # new_game.fight()


game()
