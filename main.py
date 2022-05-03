import random
import json
import time
from smash import Character, Battle

characters = []

with open('characters.json') as json_file:
    characters = json.load(json_file)

# PLAYER SELECT

player_one = None
player_two = None
# new_fight = None


def game_lobby():
    fighter_roster = []
    for x in characters:
        fighter_roster.append(x)
    print("Choose your fighter")
    # source: https://thispointer.com/python-get-first-value-in-a-dictionary/
    # prints only names of fighters
    print([list(name.items())[0][1] for name in fighter_roster])
    choose_fighter = input()
    for fighter in fighter_roster:
        if choose_fighter == fighter["name"]:
            player_one = Character(fighter["name"], 100, fighter["attacks"])
            time.sleep(1)
            print('You have chosen ' + player_one.name)
        elif not choose_fighter:
            player_random = random.choice(fighter_roster)
            player_one = Character(
                player_random["name"], 100, player_random["attacks"])
    time.sleep(1)
    computer_choice = random.choice(fighter_roster)
    player_two = Character(
        computer_choice["name"], 100, computer_choice["attacks"])
    print("Player 2 is choosing a fighter...")
    time.sleep(2)
    print('Your opponent is ' + player_two.name)
    match_start(player_one, player_two)


def match_start(player_one, player_two):
    time.sleep(1)
    print(player_one.name + " VS " + player_two.name + "!!")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("FIGHT")
    time.sleep(1)
    # new_fight = Battle(player_one, player_two)
    # print(new_fight.__dict__)
    # here is where I got stuck... my new battle class above kept coming back empty and I don't know why. So I just wrote it without it :(
    combat(player_one, player_two)


def combat(player_one, player_two):
    while player_one.hp > 0 and player_two.hp > 0:
        player_attack = player_one.choose_move()
        print(player_one.name + " uses " + player_attack["name"])
        player_two.take_dmg(player_attack["damage"])
        print("Player 2 HP = " + str(player_two.hp))
        comp_attack = player_two.choose_move()
        print(player_two.name + " uses " + comp_attack["name"])
        player_one.take_dmg(comp_attack["damage"])
        print("Player 1 HP = " + str(player_one.hp))
        win_check(player_one, player_two)
        combat(player_one, player_two)


def win_check(player_one, player_two):
    if player_one.hp <= 0:
        print(player_two.name + " is the winner!")
        time.sleep(1)
        replay()
    elif player_two.hp <= 0:
        print(player_one.name + " is the winner!")
        time.sleep(1)
        replay()


def replay():
    print("Play again? y/n")
    play_again = input()
    if play_again == "y":
        player_one = None
        player_two = None
        game_lobby()
    elif play_again == "n":
        print("See you next time!")
    else:
        print("Please enter either y or n")
        replay()


game_lobby()
