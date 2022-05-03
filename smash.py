import random

class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = 100
        self.moves = []
    
    def health_bar(self, health):
        self.health -= health 
    
    def random_move(self):
        return random.choice(self.moves)

class Battle:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2