import random

class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.start = True

class Character:
    def __init__(self, name, moves):
        self.name = name
        self.health = 50
        self.moves = moves


    def choose_move(self):
        random.choice(self.moves)

    def take_hit(self, damage):
        self.health = self.health - damage