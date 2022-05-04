import random
import json

class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def selectCharacter(self):
        self.character1 = random.choice
        self.character2 = random.choice

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health(100) 
        self.moves = []

    def decrement_health(self):
        self.health <= -10 

    def attacks(self):
        self.moves = random.choice

    
