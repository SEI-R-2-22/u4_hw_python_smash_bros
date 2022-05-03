import random
import json
import time
from smash import Character
from smash import Battle
characters = []
char_names = []
char_moves = []
winner = None



battling = True
with open('characters.json') as json_file:
    characters = json.load(json_file)

# print(characters[0]["name"])
for x in range(58):
    char_names.append(characters[x]["name"])
    char_moves.append(characters[x]["attacks"])
    

    
    # for attack in attacks:
    #     damage = attack.get("damage")
    #     atk_name = attack.get("name")


# print(char_names) 

def game():
    player1 = input("Select your character:")
    player1 = player1.lower()
    
    char_selected = False        
    if player1 in ['list', 'characters', 'LIST', 'l', 'L']:
        print('---------------------------------------')
        print(char_names)
        print('---------------------------------------')
        player1 = input("Select your character:")
        player1 = player1.lower()
        for x in characters:
            if player1 == x["name"].lower():
                char_selected = True
                player1 = x
        if char_selected == False: 
            player1 = random.choice(characters)
        player2 = random.choice(characters)
        char = Character(player1["name"], player1["attacks"])
        comp = Character(player2["name"], player2["attacks"])
        print(char.name)
        print('---------------------------------------')
        print(comp.name)
        print('---------------------------------------')
        attack = input("Attack your opponent? [y/n]")
        if attack in ['y', 'Y', 'Yes', 'YES']:
            comp.take_damage()
            comp.take_damage()
            comp.take_damage()
            char.take_damage()
            char.take_damage()
            char.take_damage()
            print("Player Health: " + str(char.health))
            print("Computer Health: " + str(comp.health))
            time.sleep(1)
            atk2 = input("Attack your opponent again? [y/n]")
            if atk2 in ['y', 'Y', 'Yes', 'YES']:
                char.take_damage()
                char.take_damage()
                char.take_damage()
                comp.take_damage()
                comp.take_damage()
                comp.take_damage()
                comp.take_damage()
                comp.take_damage()
                print("Player Health: " + str(char.health))
                print("Computer Health: " + str(comp.health))
                time.sleep(1)
                atk3 = input("Deliver the killing blow? [y/n]")
                if atk3 in ['y', 'Y', 'Yes', 'YES']:
                    char.take_damage()
                    comp.take_damage()
                    char.take_damage()
                    comp.take_damage()
                    print("Player Health: " + str(char.health))
                    print("Computer Health: " + str(comp.health))  
                if char.health == 0:
                    time.sleep(1)
                    print("Game Over {name} Wins".format(name=comp.name))
                    restart = input("Replay Game? [y/n]")
                    if restart in ['y', 'Y', 'Yes', 'YES']:
                        game()
                elif comp.health <= 0:
                    time.sleep(1)
                    print("{name}y Wins!".format(name=char.name))
                    restart = input("Replay Game? [y/n]")
                    if restart in ['y', 'Y', 'Yes', 'YES']:
                        game()      
    else:
        for x in characters:
            if player1 == x["name"].lower():
                char_selected = True
                player1 = x
        if char_selected == False: 
            player1 = random.choice(characters)
        player2 = random.choice(characters)
        char = Character(player1["name"], player1["attacks"])
        comp = Character(player2["name"], player2["attacks"])
        print(char.name)
        print('---------------------------------------')
        print(comp.name)
        print('---------------------------------------')
        attack = input("Attack your opponent? [y/n]")
        if attack in ['y', 'Y', 'Yes', 'YES']:
            comp.take_damage()
            comp.take_damage()
            comp.take_damage()
            char.take_damage()
            char.take_damage()
            char.take_damage()
            print("Player Health: " + str(char.health))
            print("Computer Health: " + str(comp.health))
            time.sleep(1)
            atk2 = input("Attack your opponent again? [y/n]")
            if atk2 in ['y', 'Y', 'Yes', 'YES']:
                char.take_damage()
                char.take_damage()
                char.take_damage()
                comp.take_damage()
                comp.take_damage()
                comp.take_damage()
                comp.take_damage()
                comp.take_damage()
                print("Player Health: " + str(char.health))
                print("Computer Health: " + str(comp.health))
                time.sleep(1)
                atk3 = input("Deliver the killing blow? [y/n]")
                if atk3 in ['y', 'Y', 'Yes', 'YES']:
                    char.take_damage()
                    comp.take_damage()
                    char.take_damage()
                    comp.take_damage()
                    print("Player Health: " + str(char.health))
                    print("Computer Health: " + str(comp.health))
                if char.health == 0:
                    time.sleep(1)
                    print("Game Over {name} Wins".format(name=comp.name))
                    restart = input("Replay Game? [y/n]")
                    if restart in ['y', 'Y', 'Yes', 'YES']:
                        game()
                elif comp.health <= 0:
                    time.sleep(1)
                    print("{name}y Wins!".format(name=char.name))
                    restart = input("Replay Game? [y/n]")
                    if restart in ['y', 'Y', 'Yes', 'YES']:
                        game()
    global battling
    battling = False
while battling == True:
    game()


