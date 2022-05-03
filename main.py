import random
import json
import smash
characters = []
replay = True
player_score = 0
comp_score = 0

with open('characters.json') as json_file:
    characters = json.load(json_file)

def game():
    player = []
    comp = []
    winner = False

    print('Character List')
    for character in characters:
        print(character["name"])
    answer = input("Select your character: ")

    for index, character in enumerate(characters):
        if character["name"].lower() == answer.lower():
            player.append(characters[index]["name"])
            player.append(characters[index]["attacks"])
            random_character = random.choice(characters)
            comp.append(random_character["name"])
            comp.append(random_character["attacks"])

    if len(player) == 0:
        random_character = random.choice(characters)
        player.append(random_character["name"])
        player.append(random_character["attacks"])
        random_character = random.choice(characters)
        comp.append(random_character["name"])
        comp.append(random_character["attacks"])

    character1 = smash.Character(player[0], player[1])
    character2 = smash.Character(comp[0], comp[1])

    print(character1.moves[random.choice(range(0,len(character1.moves)))]["name"])
    print(character1.moves[random.choice(range(0,len(character1.moves)))]["damage"])

    while not winner:
        random_move = random.choice(range(0,len(character1.moves)))

        print('{name} used {move} dealing {damage} damage.'.format(name = character1.name, move = character1.moves[random_move]["name"], damage = character1.moves[random_move]["damage"]))
        character2.decrease_health(character1.moves[random_move]["damage"])
        print('{name} life points: {health}'.format(name = character2.name, health = character2.health))      

        if character2.health <= 0:
            winner = True

        random_move = random.choice(range(0,len(character2.moves))) 
        print('{name} used {move} dealing {damage} damage.'.format(name = character2.name, move = character2.moves[random_move]["name"], damage = character2.moves[random_move]["damage"]))  
        character1.decrease_health(character2.moves[random_move]["damage"])
        print('{name} life points: {health}'.format(name = character1.name, health = character1.health))

        if character1.health <= 0:
            winner = True

    if character2.health > 0:
        # comp_score += 1
        print('Winner: {name}'.format(name = character2.name))    
        return 2

    if character1.health > 0:
        # player_score += 1
        print('Winner: {name}'.format(name = character1.name))
        return 1


while replay:
    result = game()
    if result == 1:
        player_score += 1
    elif result == 2:
        comp_score += 1

    print('Player Score: {score}'.format(score = player_score))
    print('Computer Score: {score}'.format(score = comp_score))
    answer = input("Rematch? (Y/N) ")

    if answer.lower() == 'n':
        replay = False