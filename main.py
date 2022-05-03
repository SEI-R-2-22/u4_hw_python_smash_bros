import random
import json
import time
import smash 

characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)

# for char in characters:
#     char_names.append(char['name'])



def the_game():    
    char_names = []
    for char in characters:
        char_names.append(char['name'])
 
    def random_character():
        rand = random.choice(characters)
        return smash.Character(rand['name'],rand['attacks'])

    def start_game():
        print("WELCOME TO SMASH BROS \n")
        print("(To select a character, type their name below,")
        print("or type 'list' to see list of available characters.")
        print(" To randomly select a character, leave blank)")
        res = input("\n SELECT YOUR PLAYER --> ") 


        if res=='list':
            print("\n ***** CHARACTERS ***** ")
            print(char_names)
            return start_game()
        elif not res:
            rand = random.choice(characters)
            this_player = smash.Character(rand['name'],rand['attacks'])
            return intro_battle(this_player)
        else:
            for char in characters:
                # print(char)
                if char['name'].lower() == res.lower():
                    this_player = smash.Character(char['name'], char['attacks'])
                    return intro_battle(this_player)
                # else:
                #     print(char['name'])
            
            print("Error! Character not found!")
            return start_game()


    def intro_battle(player):
        comp = random_character()

        print("\n LET THE BATTLE BEGIN! \n")

        print("~~~ " + player.name + " (player) ~~~")
        print("~~~ VERSUS ~~~")
        print("~~~ " + comp.name + " (computer) ~~~")

        return battle_time(player, comp)


    ### PRIMARY BATTLE FUNCTION

    def battle_time (player, comp):
        this_battle = smash.Battle(player, comp)

        def print_stats():
            if this_battle.winner:
                return False
            else:
                time.sleep(1)
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if player.health <=0 or comp.health <= 0:
                    print("<<< GAME!!! >>>" )
                    time.sleep(2)
                    return declare_winner()
                else:
                    print("*** CURRENT HP: ***")
                print("~~~~" + player.name + ": " + str(player.health) + " HP")
                print("~~~~" + comp.name + ": " + str(comp.health) + " HP")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(1)

        ##### PLAYER ATTACK FUNCTION #####
        def player_attack():
            print_stats()

            if this_battle.winner:
                return True
            else:
                print("\n >>>>> CHOOSE YOUR ATTACK! <<<<<")
                # print("(enter one of the following)")
                my_attacks = [x['name'] for x in player.attacks]
                print(my_attacks)
                res = input(" (type attack name, or blank for random) --> ")

                this_attack={}

                if not res:
                    this_attack = player.rand_attack()
                else:
                    for attack in player.attacks:
                        # print(attack)
                        if attack['name'].lower() == res.lower():
                            this_attack = attack
                    if this_attack == {}:
                        print("Error! Attack not found!")
                        return player_attack()

                print(player.name + " ATTACKS WITH " + this_attack['name'] + "!")
                print(comp.name + " TAKES " + str(this_attack['damage']) + " DAMAGE!")
                comp.damage(this_attack['damage'])
                this_battle.turn_count()
                return comp_attack()

            
        ##### COMPUTER ATTACK FUNCTION ######
        def comp_attack():
            print_stats()
            
            if this_battle.winner:
                return True
            else:
                print("\n>>>>>  YOUR OPPONENT IS ABOUT TO ATTACK!  <<<<<\n")
                time.sleep(1)

                my_attacks = [x['name'] for x in comp.attacks]
                this_attack = comp.rand_attack()

                print(comp.name + " ATTACKS WITH " + this_attack['name'] + "!")
                print(player.name + " TAKES " + str(this_attack['damage']) + " DAMAGE!")
                player.damage(this_attack['damage'])
                this_battle.turn_count()
                return player_attack()
                return True


        ### DECLARE A WINNER : GAME END FUNCTION 
        def declare_winner():
            this_battle.winner = True
            if player.health >0:
                print("\n⭐⭐⭐ YOU WIN! ⭐⭐⭐\n")
                this_battle.player_wins += 1
            else:
                print("\n💀💀💀 --- YOU LOSE! --- 💀💀💀 \n")
                this_battle.comp_wins += 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Final stats:")
            print("-----" + player.name + ": " + str(player.health) + "HP" + "-----" + comp.name + ": " + str(comp.health) + "HP")
            print("----- Turn count: " + str(this_battle.turns))
            return play_again()
            

        def play_again():
            res = input(">>>>> Play again? (Y/N)")
            if res.lower()=='y':
                print("This is where the game would start again!")
            else:
                print("\n THANKS FOR PLAYING \n")
                return False 

        return player_attack() if not this_battle.winner else True # BOTTOM OF GAME, FIRST ATTACK

    print("SHOULD ONLY SEE THIS ONCE")
    return start_game() # END OF THE_GAME FUNCTION

the_game() # ACTUALLY START THE GAME!