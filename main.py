import random
import json
import smash
characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)

def game():
    #choosing characters
    for character in characters:
        print(character["name"])
    print("Please select a character")
    selected_character = input()
    player_character = [character for character in characters if selected_character in character["name"]]
    if player_character == []:
        print("A random character has been chosen for you")
        player_character = random.choice(characters)
    else :
        player_character = player_character.pop()
    player = smash.Character(player_character["name"], player_character["attacks"])
    print("Your character is: " + player.name)

    opponent_character = random.choice(characters)
    opponent = smash.Character(opponent_character["name"], opponent_character["attacks"])
    print("Your opponent is: " + opponent.name)

    #battle
    duel = smash.Battle(player, opponent)
    while player.health > 0 and opponent.health > 0:
        duel.run()
    if player.health >= opponent.health:
        print("player wins")
    else :
        print("opponent wins")

game()