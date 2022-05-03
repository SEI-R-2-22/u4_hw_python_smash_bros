import random
import json


class Battle:
    def __init__(self, PC, CPU):
        self.PC = PC
        self.CPU = CPU


class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attacks = []

    def decrement_health(self, attrition):
        self.hp -= attrition
        return self.hp

    def attacks(self):
        return random.choice(self.attacks)
