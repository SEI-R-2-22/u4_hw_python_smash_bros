import random


class Character:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.attacks = attacks

    def take_dmg(self, damage):
        self.hp -= damage
        return self.hp

    def choose_move(self):
        return random.choice(self.attacks)


class Battle:
    def __init__(self, player_one, player_two):
        self.player_one: player_one
        self.player_two: player_two
