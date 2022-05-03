import random
import json
from smash import Character
from smash import Battle
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)

def game():
    x = range(0, len(characters))
    for x in characters:
        print(x['name'])

    game_character = input("Type character name from list to select:")

    character_info = [x for x  in characters if x ['name'] == game_character]

    player_character = Character(game_character, 100, character_info[0]['attacks'])
    print(f'Your character stats: {player_character.name}, {player_character.health}, {player_character.moves}')

    print("-----------------------------------------------------------------------------------------------------------")

    rand_opponent = random.choice(characters)

    opponent = Character(rand_opponent['name'], 100, rand_opponent['attacks'])
    print(f'This is the opponent: {opponent.name}, {opponent.health}, {opponent.moves}')

    print("-----------------------------------------------------------------------------------------------------------")

    if(player_character.health == 0):
        print(f'{opponent} wins!')
    elif(opponent.health == 0):
        print(f'{player_character} wins!')
    else:
        
        def player_attack():
            print(f'{player_character.name} attacks!')
            player_attack = player_character.rand_move()
            print(player_attack)
            opponent.health_bar(player_attack['damage'])
            print(f'Opponent health: {opponent.health}')

        print("-----------------------------------------------------------------------------------------------------------")

        def opponent_attack():
            print(f'{opponent.name} attacks back!')
            opponent_attack = opponent.rand_move()
            print(opponent_attack)
            player_character.health_bar(opponent_attack['damage'])
            print(f'Player health: {player_character.health}')

        print("-----------------------------------------------------------------------------------------------------------")

        player_attack()
        opponent_attack()

game()