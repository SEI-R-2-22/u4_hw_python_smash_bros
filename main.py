from calendar import c
import random
import json
import time
from smash import Character
from smash import Battle
characters = []
char_names = []

choose_char = True

game = True



with open('characters.json') as json_file:
    characters = json.load(json_file)

# for x in enumerate(characters):
#     print(x)
for x in characters:
    char_names.append(x['name'])

# print(char_names)
while (game):
    while(choose_char):
        char1 = input('\n\n\nType a characters name to select a character. If you do not know a characters name type name to see a list.\n\n')
        # print(characters['Fox'])
        if(char1.lower() == 'name'):
            for x in char_names:
                print(x)

        for n in characters:
            if char1 == n['name'].lower():
                print("FOUND CHARACTER\n\n\n")
                char1 = n
                char1 = Character(char1['name'],char1['attacks'])
                choose_char = False

    print("Choosing Opponent")
    time.sleep(.5)
    print('.')
    time.sleep(.4)
    print('.')
    time.sleep(.3)
    print('.')
    char2 = random.choice(characters)
    char2 = Character(char2['name'],char2['attacks'])

    print(char2.name + ' enters the battle. ‼️ ‼️')
    
    print('\nTime to battle')

    battle = Battle(char1,char2)

    while(battle.war):
        mv = input('Choose an attack. Type moves to see a list of moves. Or type random for a random attack.\n\n\n')
        if (mv.lower() == 'moves'):
            for x in char1.moves:
                print(x)
        elif (mv.lower() == 'rand'):
            rm = random.choice(char1.moves)
            print('You attack ' + battle.char2.name + ' with '+rm['name']+' for ' + str(rm['damage']))
            battle.char2.dec_health(rm['damage'])

        else:
            for x in char1.moves:
                if mv.lower() == x['name'].lower():
                    print('You hit ' + battle.char2.name + 'for ' + str(x['damage']))
                    battle.char2.dec_health(x['damage'])

        print(battle.char2.health)

        rm2 = random.choice(battle.char2.moves)
        print(battle.char2.name + ' attacks you with ' + rm2['name'] + ' for ' + str(rm2['damage']))
        battle.char1.dec_health(rm2['damage'])

        print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        print("You have "+str(battle.char1.health) +" left")
        print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        print("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        print("Enemy has "+str(battle.char2.health) +" left")
        print("❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎❎")
        




        if(battle.char1.health < 0 or battle.char2.health < 0):
            battle.war = False


    
    play_again = input('Type n to end the game.')
    if (play_again.lower() == 'n'):
        game = False
    else:
        choose_char = True