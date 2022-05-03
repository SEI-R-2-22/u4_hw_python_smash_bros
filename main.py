import random
import json
import time
from smash import Character, Battle

characters = []
char_names = []
player_char = {}
nme_char = {}

with open('characters.json') as json_file:
    characters = json.load(json_file)


def game():
    print('Welcome to Smash Bros!')
    time.sleep(0.5)
    print('List of playable characters incoming...')
    time.sleep(1)
    for character in characters:
        print(character["name"])
        char_names.append(character["name"].lower())
    chooseChar = input('Choose your character: ').lower()
    time.sleep(0.5)
    if chooseChar in char_names:
        for character in characters:
            if chooseChar == character["name"].lower():
                player_char = character
                print('You chose: ' + str(character["name"]))
            else:
                None
    else:
        player_char = random.choice(characters)
        print('Invalid choice, ' +
              str(player_char["name"]) + ' has been chosen for you.')
    time.sleep(0.5)
    nme_char = random.choice(characters)
    print('Your opponent is: ' + nme_char["name"])

    player = Character(player_char["name"], 25, player_char["attacks"])
    computer = Character(nme_char["name"], 25, nme_char["attacks"])

    new_game = Battle(player, computer)
    new_game.fight()
    time.sleep(1)
    replay = input('Play again? (y/n) ').lower()
    game() if (replay == 'y' or replay == 'yes') else quit()


game()
