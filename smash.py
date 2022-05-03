from email import header
import random
class Character:
    def __init__(self,name,moves):
        self.name = name
        self.health = 100
        self.moves = moves
    def dec_health(self,attack):
        self.health = self.health - attack

class Battle:
    def __init__(self,char1,char2):
        self.char1 = char1
        self.char2 = char2
        self.war = True  