import random
import json
from smash import Character, Battle

characters = []


with open('characters.json') as json_file:
    characters = json.load(json_file)

def fighter_list(choice):
    for character in characters:
        if choice == character['name']:
            return character
        return None

def game():
    for character in characters:
       print(character['name'])

    print("pick a charachter: ")
    choice = input()
    player = fighter_list(choice)

    if player == None:
        choice = random.choice(characters)
        print("you didn't chose a character, one will be chosen for you")
    else: 
        player1 = Character(player['name'], player['attacks'])

    player2choice = random.choice(characters)
    player2 = Character(player2choice['name'], player2choice['attacks'])
    print(player1.name + 'vs' + player2.name)

    battle = Battle(player1, player2)
    while battle.character1.health > 0 and battle.character2 > 0:
        attack = random.choice(['a','b'])
        if attack == 'a':
            player1move = battle.character1.random_attack()
            print(battle.character1.name + 'used' + player1move['name'] + 'it did' + str(player1move['damage']) + 'damage') 
            battle.character2.decrement_health(player1move['damage'])
        elif attack == 'b':
            player2move = battle.character2.random_attack()
            print(battle.character2.name + 'used' + player2move['name'] + 'it did' + str(player2move['damage']) + 'damage')
            battle.character1.decrement_health(player2move['damage'])

        if battle.character1.health <= 0:
            print(battle.character1.name + 'lost')
        else:
            print(battle.character2.name + 'lost')

        print('play again? yes/no')
        answer = input()
        if answer == 'yes':
            game()
        else: 
            print('thanks for playing')
game()


    
