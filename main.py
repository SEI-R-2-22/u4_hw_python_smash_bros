import random
import json
from smash import Character, Battle

characters = []
player_char = None
computer_char = None
round_count = 0

with open('characters.json') as json_file:
    characters = json.load(json_file)

# Select Characters
def character_select():
    char_list = []
    for character in characters:
        char_list.append(character["name"])
    print("LET'S SMASH! CHOOSE YOUR CHARACTER: (Press q to quit)")
    print(char_list)
    player_select = input()
    if player_select in char_list:
        for character in characters:
            if player_select == character["name"]:
                player_char = Character(character["name"], character["attacks"])
                print('Player has selected ' + player_char.name)
                break
        computer_character_select(player_char)
    else:
        print('THAT CHARACTER DOES NOT EXIST. CHOOSE A CHARACTER:')
        character_select()
        

# Select Computer
def computer_character_select(player_char):
    computer_index = random.randint(0,len(characters)-1)
    computer_char = Character(characters[computer_index]["name"],characters[computer_index]["attacks"])
    print('Computer Has Selected ' + computer_char.name)
    battle_init(player_char, computer_char)

def battle_init(player_char, computer_char):
    print("Let's battle!")
    battle = Battle(player_char, computer_char)
    make_move(battle)
# Check For Winner
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


#replay
def replay():
    print("Would you like to play again? Y/N")
    replay = input()
    if replay == 'Y':
        game()
    else:
        quit()

# Make Move
def make_move(battle):
    print(battle.player_one.name + " has " + str(battle.player_one.health) + " hitpoints remaining!")
    print(battle.player_two.name + " has " + str(battle.player_two.health) + " hitpoints remaining!")
    check_for_winner(battle)
    while battle.player_one.health > 0 and battle.player_two.health > 0:
        selected_attack_one = battle.player_one.select_attack()
        print(battle.player_one.name + " attacks with " + selected_attack_one["name"] + "!")
        print(battle.player_two.name + " takes " + str(selected_attack_one["damage"]) + " points of damage!" )
        battle.player_two.health -= selected_attack_one["damage"]
        selected_attack_two = battle.player_two.select_attack()
        print(battle.player_two.name + " attacks with " + selected_attack_two["name"] + "!")
        print(battle.player_one.name + " takes " + str(selected_attack_two["damage"]) + " points of damage!" )
        battle.player_one.health -= selected_attack_two["damage"]
        make_move(battle)

    

# Start Game
def game():
    character_select()

game()