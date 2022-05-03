import random
import json
import time
import os
from smash import *
characters = []
player_char = None
comp_char = None
round_count = 0

with open('characters.json') as json_file:
    characters = json.load(json_file)

def char_select():
    os.system('clear')
    char_list = []
    for character in characters:
        char_list.append(character["name"])

    print("Choose your fighter!\n")
    print(char_list)
    player_select = input()
    if player_select in char_list:
        for character in characters:
            if player_select == character["name"]:
                player_char = Character(character["name"], character["attacks"])
                print('Player choice: ' + player_char.name)
                break
        computer_character_select(player_char)
    else:
        print('Please choose a character that exists.')
        char_select()



def computer_character_select(player_char):
    computer_index = random.randint(0,len(characters)-1)
    computer_char = Character(characters[computer_index]["name"],characters[computer_index]["attacks"])
    print('Computer choice: ' + computer_char.name)
    battle_init(player_char, computer_char)

def battle_init(player_char, computer_char):
    print("Let's battle!")
    time.sleep(3.0)
    os.system('clear')
    battle = Battle(player_char, computer_char)
    make_move(battle)

def check_for_winner(battle):
    if battle.player_one.health <= 0 or battle.player_two.health <= 0:
        if(battle.player_one.health > battle.player_two.health):
            print(battle.player_one.name + ' Wins!')
            replay()
        elif(battle.player_one.health < battle.player_two.health):
            print(battle.player_two.name + ' Wins!')
            replay()
        elif(battle.player_one.health == battle.player_two.health):
            print(" It's a draw!")
            replay()



def replay():
    print("Would you like to play again? Y/N")
    replay = input()
    if replay.upper() == 'Y':
        game()
    else:
        quit()


def make_move(battle):
    print(battle.player_one.name + " | " + str(battle.player_one.health) + " HP ")
    print(battle.player_two.name + " | " + str(battle.player_two.health) + " HP ")
    check_for_winner(battle)
    while battle.player_one.health > 0 and battle.player_two.health > 0:
        selected_attack_one = battle.player_one.attack_select()
        print(battle.player_one.name + " attacks with " + selected_attack_one["name"])
        print(battle.player_two.name + " takes " + str(selected_attack_one["damage"]) + " damage")
        battle.player_two.health -= selected_attack_one["damage"]
        selected_attack_two = battle.player_two.attack_select()
        print(battle.player_two.name + " attacks with " + selected_attack_two["name"])
        print(battle.player_one.name + " takes " + str(selected_attack_two["damage"]) + " damage")
        battle.player_one.health -= selected_attack_two["damage"]
        make_move(battle)




def game():
    char_select()

game() 
