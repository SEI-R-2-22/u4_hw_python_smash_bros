import random

# battle and character class

class Battle:


# need name, health, and list of their moves 

class Character:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks 
    def decrement_health(self, other):
        self.health -= other.attacks.damage
        print self.health
    def attack(self, other):
        self.attacks = random.self.attacks
        other.health -= self.attacks.damage 

