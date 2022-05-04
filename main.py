import random
import json
from smash import Battle, Character

characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)

def get_characters(playerchoice):
    for character in characters:
        if playerchoice == character["name"]:
            return character
    return None

def game():
    for character in characters:
        print(character['name'])
    
    print("Choose your Character!")
    playerchoice = input()
    player = get_characters(playerchoice)

    if player == None:
        playerchoice = random.choice(characters)
        player1 = Character(playerchoice['name'], playerchoice['attacks'])
        print("!!!!!!!!!!!!##############!!!!!!!!!!!!!!")
        print("Check your spelling. You have been assigned " + playerchoice["name"] + " because no characters matched what you input")
    else:
        player1 = Character(player['name'], player['attacks'])
        
    player2choice = random.choice(characters)
    player2 = Character(player2choice['name'], player2choice['attacks'])
    print(player1.name + " VERSUS " + player2.name + " FIGHT!!!")

    fight = Battle(player1, player2)
    while fight.character_one.health > 0 and fight.character_two.health > 0:
        attack = random.choice([1,2])
        if attack == 1:
            player1attack = fight.character_one.random_attack()
            print(fight.character_one.name + " attacks with " + player1attack["name"] + " and it does " + str(player1attack["damage"]) + " Damage")
            fight.character_two.decrement_health(player1attack["damage"])
        elif attack == 2:
            player2attack = fight.character_two.random_attack()
            print(fight.character_two.name + " attacks with " + player2attack["name"] + " and it does " + str(player2attack["damage"]) + " Damage")
            fight.character_one.decrement_health(player2attack["damage"])

    if fight.character_one.health <= 0:
        print(fight.character_one.name + " has been defeated")
    else: 
        print(fight.character_two.name + " has been defeated")
    
    print("Play again? [y/n]")
    response = input()
    if response == "y" or response == "Y":
        game()
    else:
        print("Goodbye!") 
    


game()

