import random


class Character:
    def __init__(self, char_name, attacks):
        self.char_name = char_name
        self.attacks = attacks
        self.health = 100

    def attack(self, attack):
        self.health -= attack

    def random_attack(self):
        return random.choice(self.attacks)


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def battle(self):
        if self.player1.health > 0 and self.player2.health > 0:
            self.player1.attack(self.player2)
            self.player2.attack(self.player1)
        if self.player1.health <= 0:
            print('player2 wons')
        elif self.player2.health <= 0:
            print('player1 won!')
