import random
import json


class Battle:
    def __init__(self):
        pass


class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attacks = []

    def decrement_health(self, attrition):
        self.health -= attrition
        return self.health

    def attacks(self):
        self.random.attacks
