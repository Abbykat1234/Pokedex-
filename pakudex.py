"""import statement so that I can access the class Pakuri to create an instance of the class"""
from pakuri import Pakuri


class Pakudex:
    """initializing method that initilizes the object to contain exactly the capacity of 20
    objects when it is completely full. Default capacity for the pakudex is 20"""
    """sets the capacity based on the capacity that we pass in. Decides how big our list could be"""
    pakuris = []
    size = 0
    def __init__(self, capacity=20):
        self.capacity = capacity  # initial capacity value is 20
        """creates an empty list of pakuri objects that can be added to using the add_pakuri() function"""
        """size attribute/variable"""
        """keeps track of the concrete number of pkauri objects in the list self.pakuris"""

    """getter method that retrieves & returns the size of the pakudex or the number of critters 
    currently being stored in the pakudex"""
    def get_size(self):
        return len(self.pakuris)

    """getter method that retrieves & returns the capacity of the pakudex"""
    def get_capacity(self):
        return self.capacity

    """method that returns a string list containing the species of the critters as ordered in the pakudex.
    If there are no species added yet, the method will return None"""
    def get_species_array(self):
        """loop through self.pakuris to look at each pakuri object"""
        """declares & initilizes an empty list"""
        res = []
        """instances of an object are lowercase. Lowercase of the class."""
        for pakuri in self.pakuris:
            """append the pakuri.species object to the result list"""
            """want to retrieve one attribute from the box, which is the species & and all the species 
            from different pakuri objects to my result list"""
            res.append(pakuri.species)
        """returns the string list called res when the method is called"""
        return res

    """method that sorts the pakuri objects in the pakudex according to Python standard lexographical
    ordering of species name."""
    def sort_pakuri(self):
        """sorted is a built-in python function that orders objects in alphabetical order"""
        """sorts the pakuri objects"""
        self.pakuris.sort(key=lambda pakuri: pakuri.species)


    """getter method that returns an integer list containing the attack, defense, and speed statistics of 
    species. If the species is not in the pakudex, it returns None"""
    def get_stats(self, species):
        """initializes an integer list called stats to empty"""
        stats = []

        """loops through self.parkuris to look at each pakuri object"""
        for pakuri in self.pakuris:
            """compares pakuri.species to the species being passed in"""
            if pakuri.species == species:
                stats.append(pakuri.get_attack())
                stats.append(pakuri.get_defense())
                stats.append(pakuri.get_speed())
                return stats

        return None


    """method that adds species to the pakudex. If it is successful, it will return true. If not, returns
    false. Species is a string that is part of the Parkuri object."""
    def add_pakuri(self, species):
        """1. determine what we can add by checking for duplicates. If it is a duplicate, the method
        will return false"""
        if species in self.get_species_array():
            print("Error: Pakudex already contains this species!")
            return False

        """2. check if the list is full. The method will return false if this is true"""
        if self.size == self.capacity:
            return False

        else:
            """adds Pakuri object to the Pakudex list"""
            """create a Pakuri object by calling the constructor and passing in the species"""
            """append to the end of the current list the newly created Pakuri object"""
            pak = Pakuri(species)
            self.pakuris.append(pak)
            self.size += 1
            """want to increment the size of the Pakudex to be one larger since we added one 
            species to the list. We also want the method to return true"""
            """returns true"""
            """prints out the message that the species of Pakuri was successfully added to the 
            Pakudex list"""
            print(f'Pakuri species {species} successfully added!')
            return True

    """method that attempts to evolve species within the pakudex. If it is successful, the method
    returns true. If it is unsuccessful, the method returns false."""
    def evolve_species(self, species):
        """calls on the method evolve(self) befinded in the pkauri.py file & applies that meethod
        to the pakuri objects in the pakudex."""
        """if the species that we want to evolve is in the pakudex, then this method evolves it 
        & returns true"""
        """self.pakuris is a list of pakuri objects"""
        "know that the species is inside of the list, but did not find its location"
        if species in self.get_species_array():
            for pakuri in self.pakuris:
                if pakuri.species == species:
                    pakuri.evolve()
                    print(f"{species} has evolved!")
            return True
        else:
            """if the species does not exist, then this method returns false and prints 
            out the message, "No such Pakuri!"""
            print("No such Pakuri!")
            return False

