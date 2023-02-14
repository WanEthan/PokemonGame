"""
Yu Jen Wan (Ethan)
Foothill College, CS3B, 2022
Project 3 - Pokemon Game
Let users create their own type of pokemon to fight against the
opponent's Pokemon.

"""

from DisPokemonWan import *
from ghosttype import *


class PokeGame:
    """ Create a new class for the opponent's Pokemon """

    def __init__(self):
        """ Call the setup method and game_master (empty list)
        as an instance attribute

        """
        self.game_master = []
        self.setup()

    def setup(self):
        """ Add the seven instances into the game_master list """
        self.game_master = [
            Water("Wartortle", "Sophia", 50),
            GhostType("Charmander", "John", 40),
            GhostType("Pikachu", "Ryan", 60),
            Water("Blastoise", "Jack", 80),
            Water("Poliwhirl", "Ethan", 100),
            Water("Raichu", "Emma", 70),
            GhostType("Vulpix", "Olivia", 90)]

    def draw_pokemon(self):
        """ Remove an instance from the list of Pokemon by using pop()
        method and print the selected instance
        returns the Pokemon instance

        """
        if self.game_master:
            selected_pokemon = self.game_master.pop()
            print(f"\nThis pokemon will be your opponent's Pokemon \n"
                  f"{selected_pokemon}")
            return selected_pokemon
        print(f"\nGame Over!!")  # When there is no more instances in the list


def menu():
    """ Display all valid Pokemon types """
    print(f"----------------------------")
    print(f"Here are valid Pokemon types")
    print(f"1 - Water type")
    print(f"2 - Ghost Type")
    print(f"----------------------------")


def main():
    """ Let users make a Pokemon and call the attack method and pass
    the opponent's Pokemon instance

    """
    poke_game = PokeGame()
    while True:  # Play the game until the list has no instance
        opponent = poke_game.draw_pokemon()
        if opponent is None:
            break
        menu()
        selected_type = input(f"Please choose a Pokemon type you would like "
                              f"to play! ")
        try:
            selected_type = int(selected_type)  # convert str to int
        except ValueError:
            print(f"This is not a number!")
            continue
        if selected_type == 1:
            the_name = input(f"What would like to call your Pokemon? ")
            the_trainer = input(f"Please enter your name as the Pokemon "
                                "trainer ")
            hp = input(f"How much HP do you want to give your Pokemon? (0 to "
                       "100) ")
            print(f"")
            player_instance = Water(the_name, the_trainer, hp)
            player_instance.attack(opponent)
        elif selected_type == 2:
            the_name = input(f"What would like to call your Pokemon? ")
            the_trainer = input(f"Please enter your name as the Pokemon "
                                "trainer ")
            hp = input(f"How much HP do you want to give your Pokemon? (0 to "
                       "100) ")
            print(f"")
            player_instance = GhostType(the_name, the_trainer, hp)
            player_instance.attack(opponent)
        else:
            print(f"This number is not on the menu!")


if __name__ == "__main__":
    main()


"""
----------------Sample Run----------------
This pokemon will be your opponent's Pokemon 
Olivia's Ghost Pokemon Vulpix0.3 probablity of paralyzing the opponent.
----------------------------
Here are valid Pokemon types
1 - Water type
2 - Ghost Type
----------------------------
Please choose a Pokemon type you would like to play! 1
What would like to call your Pokemon? Psyduck
Please enter your name as the Pokemon trainer lan
How much HP do you want to give your Pokemon? (0 to 100) 20

Psyduck!
Psyduck  used  Splishy Splash !
Vulpix is paralyzed!

This pokemon will be your opponent's Pokemon 
The Pokemon's name: Raichu 
The Pokemon's trainer: Emma 
HP: 70 
The basic_attack: Splishy Splash 
Probability 0.3 

----------------------------
Here are valid Pokemon types
1 - Water type
2 - Ghost Type
----------------------------
Please choose a Pokemon type you would like to play! 2
What would like to call your Pokemon? Muk
Please enter your name as the Pokemon trainer Amy
How much HP do you want to give your Pokemon? (0 to 100) 40

Muk!
Muk  used  lick !

This pokemon will be your opponent's Pokemon 
The Pokemon's name: Poliwhirl 
The Pokemon's trainer: Ethan 
HP: 100 
The basic_attack: Splishy Splash 
Probability 0.3 

----------------------------
Here are valid Pokemon types
1 - Water type
2 - Ghost Type
----------------------------
Please choose a Pokemon type you would like to play! 1
What would like to call your Pokemon? Shellder
Please enter your name as the Pokemon trainer Harry
How much HP do you want to give your Pokemon? (0 to 100) 50

Shellder!
Shellder  used  Splishy Splash !

This pokemon will be your opponent's Pokemon 
The Pokemon's name: Blastoise 
The Pokemon's trainer: Jack 
HP: 80 
The basic_attack: Splishy Splash 
Probability 0.3 

----------------------------
Here are valid Pokemon types
1 - Water type
2 - Ghost Type
----------------------------
Please choose a Pokemon type you would like to play! 2
What would like to call your Pokemon? Gastly
Please enter your name as the Pokemon trainer Mark
How much HP do you want to give your Pokemon? (0 to 100) 10

Gastly!
Gastly  used  lick !
Blastoise is paralyzed

This pokemon will be your opponent's Pokemon 
Ryan's Ghost Pokemon Pikachu0.3 probablity of paralyzing the opponent.
----------------------------
Here are valid Pokemon types
1 - Water type
2 - Ghost Type
----------------------------
Please choose a Pokemon type you would like to play! 1
What would like to call your Pokemon? Horsea
Please enter your name as the Pokemon trainer Paul
How much HP do you want to give your Pokemon? (0 to 100) 40

Horsea!
Horsea  used  Splishy Splash !

This pokemon will be your opponent's Pokemon 
John's Ghost Pokemon Charmander0.3 probablity of paralyzing the opponent.
----------------------------
Here are valid Pokemon types
1 - Water type
2 - Ghost Type
----------------------------
Please choose a Pokemon type you would like to play! 2
What would like to call your Pokemon? Misdreavus
Please enter your name as the Pokemon trainer Ted
How much HP do you want to give your Pokemon? (0 to 100) 55

Misdreavus!
Misdreavus  used  lick !
Charmander  fainted!

This pokemon will be your opponent's Pokemon 
The Pokemon's name: Wartortle 
The Pokemon's trainer: Sophia 
HP: 50 
The basic_attack: Splishy Splash 
Probability 0.3 

----------------------------
Here are valid Pokemon types
1 - Water type
2 - Ghost Type
----------------------------
Please choose a Pokemon type you would like to play! 1
What would like to call your Pokemon? Qwilfish
Please enter your name as the Pokemon trainer Eric
How much HP do you want to give your Pokemon? (0 to 100) 60

Qwilfish!
Qwilfish  used  Splishy Splash !

Game Over!!

Process finished with exit code 0

"""