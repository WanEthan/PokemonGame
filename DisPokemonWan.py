"""
Yu Jen Wan (Ethan)
Foothill College, CS3B, 2022
Using inheritance to create the relationship between a child class (a
type of pokemon) and its parent class (the Pokemon class)

"""

from pokemon import *
from random import random


class Water(Pokemon):
    """ Create a new class for water type pokemon """

    def __init__(self, name, trainer, hp):
        """ Inherited from the Pokemon class and add hp, basic_attack
        prob and damage as instance attributes

        """
        super().__init__(name, trainer)
        self.hp = hp
        self.basic_attack = "Splishy Splash"
        self.damage = 40
        self.pro = 0.3

    def __str__(self):
        """ Return f-string containing the basic information of the
        water type pokemon

        """
        return f"The Pokemon's name: {self.name} \nThe Pokemon's trainer: " \
               f"{self.trainer} \nHP: {self.hp} \nThe basic_attack: " \
               f"{self.basic_attack} \nProbability {self.pro } \n"

    def attack(self, other):
        """  Use isinstance to check the instance type (Pokemon) """
        Pokemon.attack(self, other)
        if not isinstance(other, Water) and random() < self.pro:
            other.paralyzed = True
            print(f"{other.name} is paralyzed!")


def main():
    """ Creat an instance of the Water type class """
    p1 = Water("Ethan", "Ethan", 100)
    print(p1)


if __name__ == "__main__":
    main()
