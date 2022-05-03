import random
import json
from smash import Battle, Character
characters = []
player_1 = []
player_2 = []
battle = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def new_character(player_1_choice):
    for character in characters:
        if player_1_choice == character['name']:
            return character


def rand_player():
    player_2_choice = random.choice(characters)
    player_2 = Character(player_2_choice['name'], player_2_choice['moves'])
    return player_2


def battle_start(player_1, player_2):
    choice = input(
        'Start Battle! (y) Re-Select Character (n)'
    )
    if choice == 'n':
        return Battle(player_1, player_2)
    elif choice == 'y':
        game()


def restart():
    choice = input('Play Again?(y/n)')
    if choice == 'y':
        game()
    elif choice == 'n':
        print('GoodBye!')
        restart()


def game():
    for character in characters:
        print(character['name'])
    player_1_choice = input('Select a Character')
    player_1 = new_character(player_1_choice)
    if player_1 == None:
        player_1_choice = random.choice(characters)
        player_1 = Character(
            player_1_choice['name'], player_1_choice['moves']
        )
    else:
        player_1 = Character(player_1['name'], player_1['moves'])
        print('you selected' + player_1.name)

    player_2 = rand_player()

    print('you will fight' + player_2.name)
    battle = battle_start(player_1, player_2)


while battle.p1.health and battle.p2.health > 0:
    print(battle.p1.name + battle.p1.health + 'HP')
    print(battle.p2.name + battle.p2.health + 'HP')
    print(battle.p1.name + 'coming up')
    player_1_move = battle.p1.rand_attack()
    print(player_1_move['name'])
    battle.p2.decrement_health(player_1_move['damage'])
    print(battle.p2.health + 'HP')
    if battle.p2.health <= 0:
        print(battle.p2.name + 'Died')
        restart()
        break
    print(battle.p2.name + 'coming up')
    player_2_move = battle.p2.rand_attack()
    print(player_2_move['name'])
    battle.p1.decrement_health(player_2_move['damage'])
    print(battle.p1.health + 'HP')
    if battle.p1.health <= 0:
        print(battle.p1.name + 'Died')
        restart()
