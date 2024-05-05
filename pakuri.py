"""this class is the blueprint for the different critter objects that will be created."""
"""this class will store information about the critter's species, attack level, defense level, 
and speed"""


class Pakuri:
    """method that initializes all the species attributes of the pakuri object """
    """passes in species into the self.species"""
    def __init__(self, species):
        """species, attack, & speed are initialized to the values in the attribute table of the
        project instructions"""
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    """getter method that retrieves and returns the species of the critter"""
    def get_species(self):
        return self.species

    """getter method that retrieves and returns the attack value for the critter"""
    def get_attack(self):
        return self.attack

    """getter method that retrieves and returns the defense value for the critter"""
    def get_defense(self):
        return self.defense

    """getter method that retrieves and returns the speed value for the critter"""
    def get_speed(self):
        return self.speed

    """setter method that sets the value of the attack attribute of the critter. It
    sets the value of attack to new_attack"""
    def set_attack(self, new_attack):
        """for this instance of the class, self"""
        self.attack = new_attack

    """method that evolves the critter as follows: a)doubles the attack, b) quadruples the defense,
    c) triples the speed"""
    """program needs self. because it needs the object that it is modifying"""
    def evolve(self):
        self.attack = self.attack * 2
        self.defense = self.defense * 4
        self.speed = self.speed * 3
