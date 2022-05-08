import random
from smash import Battle, Character

CHARACTER_ROSTER = [
    Character('Pikachu', [
        {'name': 'thunderbolt', 'damage': 10},
        {'name': 'tail whip', 'damage': 3},
        {'name': 'tackle', 'damage': 1},
    ]),
    Character('Link', [
        {'name': 'jab', 'damage': 1},
        {'name': 'gale boomerang', 'damage': 10},
        {'name': 'jab3', 'damage': 3},
    ]),
    Character('Wario', [
        {'name': 'dash attack', 'damage': 7},
        {'name': 'fsmash', 'damage': 10},
        {'name': 'bair', 'damage': 12},
    ]),
    Character('Metaknight', [
        {'name': 'fsmash', 'damage': 17},
        {'name': 'ftilt', 'damage': 3},
        {'name': 'drill rush', 'damage': 1},
    ]),
    Character('Lucas', [
        {'name': 'pk fire', 'damage': 3},
        {'name': 'uair', 'damage': 13},
        {'name': 'psi magnet', 'damage': 8},
    ]),
    Character('Kirby', [
        {'name': 'fsmash', 'damage': 15},
        {'name': 'inhale', 'damage': 1},
        {'name': 'uthrow', 'damage': 10},
    ]),
    Character('Falco', [
        {'name': 'rapid jab finisher', 'damage': 3},
        {'name': 'fsmash', 'damage': 15},
        {'name': 'uair', 'damage': 10},
    ]),
    Character('Diddykong', [
        {'name': 'utilt', 'damage': 6},
        {'name': 'banana peel', 'damage': 3},
        {'name': 'bthrow', 'damage': 10},
    ]),
    Character('CaptainFalcon', [
        {'name': 'utilt', 'damage': 6},
        {'name': 'rapid jab finisher', 'damage': 2},
        {'name': 'falcon punch', 'damage': 25},
    ]),
]


def player_character_selection():
    print("|  CHOOSE YOUR FIGHTER!  |")
    for index, character in enumerate(CHARACTER_ROSTER):
        print(f'{index + 1}. {character.name}')

    selection = input("Enter your selection here: ").strip()

    if selection.isdigit() and 0 < int(selection) <= len(CHARACTER_ROSTER):
        character = CHARACTER_ROSTER[int(selection) - 1]
        print(f'Congrats, you chose {character.name}!')

    else:
        character = random_character_selection()
        print(
            f' \033[91m{selection}\033[0m is not valid, so we chose {character.name} for you!')
    return character


def computer_character_selection():
    character = random_character_selection()
    print(f'You will be facing off against {character.name}')
    return character


def random_character_selection():
    return random.choice(CHARACTER_ROSTER)


def game():
    print("Welcome to the SUPER SMASH BROS tournament!")
    player_character = player_character_selection()
    computer_character = computer_character_selection()
    victor = Battle([player_character, computer_character]).start_battle()
    print(
        f'What a show tonight. It was down to the wire, but {victor.name} was victorious! Thanks for playing!')


if __name__ == '__main__':
    game()
