import random

class Character:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves
    
    def health_bar(self, attack):
        self.health = int(self.health - int(attack))
    
    def rand_move(self):
        index = random.randint(0, len(self.moves))
        return self.moves[index]

class Battle:
    def __init__(self, chara1, chara2):
        self.chara1 = chara1
        self.chara2 = chara2