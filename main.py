import random
import json
import smash
characters = []
player_score = 0
comp_score = 0

with open('characters.json') as json_file:
    characters = json.load(json_file)

def start_game():
    player = []
    comp = []
    winner = False

    print("Character List")
    for character in characters:
        print(character["name"])
    answer = input("Who would you like to choose?")

    for index, character in enumerate(characters):
        if character["name"].lower == answer.lower():
            player.append(characters[index]["name"])
            player.append(characters[index]["attacks"])
            random_character = random.choice(characters)
            comp.append(random_character["name"])
            comp.append(random_character["attacks"])

        
        character1 = smash.Character(player[0], player[1])
        character2 = smash.Character(comp[0], comp[1])

        start = smash.Battle(character1, character2)

        if start.start:
            while not winner:
                random_move = character1.choose_move()

                print('You have taken {damage} damage from {name}')
                character2.take_hit(random_move["damage"])
                
                if character2.health <= 0:
                    winner = True

                random_move = character2.select_move()
                print('You have taken {damage} damage from {name}')
                character1.take_hit(random_move["damage"])

                if character1 <= 0:
                    winner = True

            if character2.health > 0:
                print('Winner: {name}')

            if character1.health > 0:
                print('Winner: {name}')

        
        else:
            print("Please choose character first")

