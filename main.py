from smash import Character, Battle
import sys
import random
import json
sys.path.append(".")


with open('characters.json') as json_file:
    characters = json.load(json_file)
    moves_by_character_dict = {}
    for character in characters:
        moves_by_character_dict.update(
            {character["name"]: character["attacks"]})

    print('Welcome to Smash Bros! Here are the available characters: ')
    for character in characters:
        print(character["name"])

    player_character_name = input('Choose your character: ')

    print(f'You have chosen: {player_character_name}')
    # print("Their moves are:" + str(moves_by_character_dict[player_character_name]))

    computer_character = random.choice(characters)
    computer_character_name = computer_character["name"]

    print("Computer has chosen: " + computer_character_name)

    character1 = Character(player_character_name, 100,
                           moves_by_character_dict[player_character_name], 0)
    character2 = Character(computer_character_name, 100,
                           moves_by_character_dict[computer_character_name], 0)

    battle = Battle(character1, character2, False)

    battle.start_battle()


# Joey = Animal('Joey', 'Terrier', [])
