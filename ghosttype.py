"""
Jonathon Green
Foothill College, CS3B, Summer 2022
Assignment: Pokemon Discussion Assignment
7-13-2022

Ghost type pokemon.
"""

from random import random
from pokemon import Pokemon


class GhostType(Pokemon):
    """
      An instance of this class represents a ghost type pokemon.
    """

    basic_attack = "lick"
    prob = .3

    def __init__(self, name, trainer, hp):
        super().__init__(name, trainer)

        self.hp = hp

    def __str__(self) -> str:
        return f"{self.trainer}'s Ghost Pokemon {self.name}" \
            f"{self.prob} probablity of paralyzing the opponent."

    def attack(self, other):
        super().attack(other)

        if not isinstance(other, GhostType) and random() < self.prob:
            other.paralyzed = True
            print(f'{other.name} is paralyzed')


if __name__ == '__main__':
    kangaskhan = Pokemon('Kanga', 'Stacy')
    print(kangaskhan)
    polteageist = GhostType('Earl', 'Jon', 45)
    print(polteageist)

    polteageist.attack(kangaskhan)
    kangaskhan.attack(polteageist)
    polteageist.attack(kangaskhan)
    kangaskhan.attack(polteageist)
