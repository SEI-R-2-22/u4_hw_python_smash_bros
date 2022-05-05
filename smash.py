import random

class Character:
    def __init__(self, name, list):
        self.name = name
        self.health = 20
        self.attacks = list

    def damage(self, hp):
        self.health -= hp

    def rand_attack(self):
        return random.choice(self.attacks)


class Battle:
    def __init__(self, player_one, player_two):
        self.player = player_one
        self.npc = player_two