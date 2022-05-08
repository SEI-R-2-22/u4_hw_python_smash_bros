import random

DEFAULT_CHARACTER_HEALTH = 50


class Battle(object):
    def __init__(self, battlers):
        self.battlers = battlers
        random.shuffle(self.battlers)
        print(f'{self.battlers[0].name} goes first!')

    def start_battle(self):
        while True:
            self.battlers[0].attack(self.battlers[1])
            if self.battlers[1].health <= 0:
                return self.battlers[0]
            self.battlers[1].attack(self.battlers[0])
            if self.battlers[0].health <= 0:
                return self.battlers[1]


class Character(object):
    def __init__(self, name, attack_list, max_health=DEFAULT_CHARACTER_HEALTH):
        self.name = f'\033[94m{name}\033[0m'
        self.attack_list = attack_list
        self.max_health = self.health = max_health

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f'{self.name} has \033[96m{self.health}\033[0m remaining!')

    def attack(self, opponent):
        attack = random.choice(self.attack_list)
        print(
            f'{self.name} \033[92m{attack["name"]}\033[0m for \033[93m{attack["damage"]}\033[0m! This could be serious!')
        opponent.take_damage(attack['damage'])
