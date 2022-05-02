import random
import json
from smash import Character, Battle

characters = []
player_one = []
player_two = []
battle = []

with open('characters.json') as json_file:
    characters = json.load(json_file)


def find_character(player_one_choice):
    for character in characters:
        if player_one_choice == character['name']:
            return character
    return None


def random_player():
    player_two_choice = random.choice(characters)
    player_two = Character(
        player_two_choice['name'], player_two_choice['attacks'])
    return player_two


def battle_start(player_one, player_two):
    choice = input(
        'Ready to battle, or would you like to choose again? (battle/repick)')
    if choice == 'battle':
        return Battle(player_one, player_two)
    elif choice == 'repick':
        game()
    else:
        print('That is not a valid choice, please choose again.')
        battle_start(player_one, player_two)


def play_again():
    choice = input('Would you like to play again? (yes/no)')
    if choice == 'yes':
        game()
    elif choice == 'no':
        print('Thank you for playing!')

    else:
        print('That is not a valid choice.  Please pick again.')
        play_again()


def game():
    print("""Welcome to GA-Smash""")
    for character in characters:
        print(character['name'])
    player_one_choice = input("Please choose a character")
    player_one = find_character(player_one_choice)
    if player_one == None:
        player_one_choice = random.choice(characters)
        player_one = Character(
            player_one_choice['name'], player_one_choice['attacks'])
        print("That wasn't a valid selection.  You are now: " + player_one.name)
    else:
        player_one = Character(player_one['name'], player_one['attacks'])
        print('You have selected: ' + player_one.name)

    player_two = random_player()

    print('You will be fighting: ' + player_two.name)
    battle = battle_start(player_one, player_two)

    while battle.char_one.health > 0 and battle.char_two.health > 0:
        print(battle.char_one.name + ' is at ' +
              str(battle.char_one.health) + ' health')
        print(battle.char_two.name + ' is at ' +
              str(battle.char_two.health) + ' health')
        print(battle.char_one.name + ' is up!')
        player_one_attack = battle.char_one.random_attack()
        print(battle.char_one.name + ' attacks with ' +
              player_one_attack['name'] + '! It does ' + str(player_one_attack['damage']) + ' damage!')
        battle.char_two.lose_health(player_one_attack['damage'])
        print(battle.char_two.name + ' is now at ' +
              str(battle.char_two.health) + ' health.')
        if battle.char_two.health <= 0:
            print(battle.char_two.name + ' is ded.')
            play_again()
            break
        print(battle.char_two.name + ' is up!')
        player_two_attack = battle.char_two.random_attack()
        print(battle.char_two.name + ' attacks with ' +
              player_two_attack['name'] + '! It does ' + str(player_two_attack['damage']) + ' damage!')
        battle.char_one.lose_health(player_two_attack['damage'])
        print(battle.char_one.name + ' is now at ' +
              str(battle.char_one.health) + ' health.')
        if battle.char_one.health <= 0:
            print(battle.char_one.name + ' is ded')
            play_again()
            break


game()
