import random
import json


class Mario:
    def __init__(self):
        self.health = 100
        self.moves = {
            'jump': 10,
            'hammer': 6
        }

    def attack(self, move):
        """
        Returns the amount of damage a move does. If the move doesn't exist or if the player ran out
        of those moves, this will return 0. If the move is valid, it will return the amount of damage it will do.

        move => String
        returns => Int
        """

        try:
            if self.moves[move] <= 0:
                return 0
        except KeyError:
            return 0
        else:
            extra_damage = random.randint(1, 5)
            with open('move_damage.json') as damage_file:
                return json.loads(damage_file.read())[move] + extra_damage
