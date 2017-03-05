import random
import json


class Enemy:
    def __init__(self):
        self.health = 0
        self.class_name = ''

    def attack(self, move):
        try:
            with open('move_damage.json') as damage_file:
                json.loads(damage_file.read())[self.class_name].index(move)
        except IndexError:
            raise ValueError("Hmm... The \"attack\" method seems to be taking in an invalid move.")
        else:
            extra_damage = random.randint(-1, 4)
            with open('move_damage.json') as damage_file:
                return json.loads(damage_file.read())[self.class_name][move] + extra_damage


class Goomba(Enemy):
    def __init__(self):
        self.health = 20
        self.class_name = 'Goomba'


class KoopaTroopa(Enemy):
    def __init__(self):
        self.health = 45
        self.class_name = 'KoopaTroopa'


class ShyGuy(Enemy):
    def __init__(self):
        self.health = 30
        self.class_name = 'ShyGuy'
