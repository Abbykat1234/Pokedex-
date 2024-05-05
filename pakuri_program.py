"""this file is the driver. When run it will do the following: (1) display a welcome message,
(2) prompt for/read pakudex capacity & confirm, (3) display the menu, and (4) prompt for input"""
from pakudex import Pakudex

"""creates a Pakudex object"""


def main():
    """Displays the welcome message"""
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    """prompt for/read pakudex capacity & confirm"""
    capacity = input("Enter max capacity of the Pakudex: ")
    if capacity.isdigit():
        pakudex = Pakudex(int(capacity))
        print(f"The Pakudex can hold {capacity} species of Pakuri.")
    else:
        while not capacity.isdigit():
            print("Please enter a valid size. ")
            capacity = input("Enter max capacity of the Pakudex: ")
            if capacity.isdigit():
                capacity = int(capacity)
                pakudex = Pakudex(capacity)
                print(f"The Pakudex can hold {capacity} species of Pakuri.")
                break

    while True:
        """Displays the menu"""
        print()
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")

        """prompts the user for input"""
        print()
        user_choice = input("What would you like to do? ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
        else:
            while not user_choice.isdigit():
                print("Unrecognized menu selection!")
                user_choice = (input("What would you like to do?"))
                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    break

        """if statements that decide which methods to run based off of the user input"""
        if user_choice == 1:
            """calls the method get_species_carray so that the pakuri that are currently 
            in the pakudex are listed and printed out"""
            res = pakudex.get_species_array()
            if len(res) == 0:                  
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i in range(len(res)):
                    print(f'{i + 1}. {res[i]}')
        elif user_choice == 2:
            """prompts the user to for a species a stores it in the string variable species"""
            species = input("Enter the name of the species you would like to display: ")
            if pakudex.get_stats(species) == None:
                print("Error: No such Pakuri!")
            else:
                stats = pakudex.get_stats(species)
                print(f'Species: {species}')
                print(f'Attack: {stats[0]}')
                print(f'Defense: {stats[1]}')
                print(f'Speed: {stats[2]}')
        elif user_choice == 3:
            """prompts the user for the name of the species to add to the Pakudex"""
            if pakudex.size == pakudex.capacity:
                print("Error: Pakudex is full")
            else:
                species = input("Enter the name of the species to add: ")
                """call to the method add_pakuri()"""
                pakudex.add_pakuri(species)
        elif user_choice == 4:
            """prompts the user to enter the name of the species they want to evolve"""
            species = input("Enter the name of the species to evolve: ")
            """call to the method evolve(self, species)"""
            pakudex.evolve_species(species)
        elif user_choice == 5:
            """call to the method sort_pakuri(self)"""
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
        elif user_choice == 6:
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")


if __name__ == '__main__':
    """call to the main() method"""
    main()
