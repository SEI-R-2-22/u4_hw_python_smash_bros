import random


class Battle: 
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        


class Character:
    def __init__(self, name, attacks):
        self.name = name
        self.attacks = attacks
        self.health = 100

    def get_hit(self, attack):
        self.health += attack
        return self.health

    def attack_select(self):
        random_index = random.randint(0, len(self.attacks)-1)
        spec_attack = self.attacks[random_index]
        return spec_attack
        