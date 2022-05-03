import random
import json
import time
characters = []
wins = 0
losses = 0

with open('characters.json') as json_file:
    characters = json.load(json_file)


class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves

    def new_attack(self, attack):
        self.moves.append(attack)

    def dec_health(self, dec):
        self.health -= dec

    def random_atk(self):
        return (random.choice(self.moves))


class Battle:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def fight(self):
        num_arr = [0, 1]
        global wins
        global losses

        def char1_turn():
            time.sleep(0.5)
            char1_atk = (self.char1.random_atk())
            self.char2.dec_health(char1_atk["damage"])
            print(self.char1.name + ' used ' +
                  char1_atk["name"] + ' for ' + str(char1_atk["damage"]) + ' damage! ' + self.char2.name + ' at ' + str(self.char2.health) + ' health.')

        def char2_turn():
            time.sleep(0.5)
            char2_atk = (self.char2.random_atk())
            self.char1.dec_health(char2_atk["damage"])
            print(self.char2.name + ' used ' +
                  char2_atk["name"] + ' for ' + str(char2_atk["damage"]) + ' damage! ' + self.char1.name + ' at ' + str(self.char1.health) + ' health.')

        while self.char1.health > 0 and self.char2.health > 0:
            turn = random.choice(num_arr)
            if (turn == 0):
                char1_turn()
                char2_turn() if (self.char2.health > 0) else None
            else:
                char2_turn()
                char1_turn() if (self.char1.health > 0) else None

        if (self.char1.health > 0):
            time.sleep(1)
            print('Winner is Player as ' + self.char1.name)
            wins += 1
            print('Wins: ' + str(wins))
            print('Losses: ' + str(losses))
        else:
            time.sleep(1)
            print('Winner is Computer as ' + self.char2.name)
            losses += 1
            print('Wins: ' + str(wins))
            print('Losses: ' + str(losses))
