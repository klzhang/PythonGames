import random

class Pokemon:

    def __init__(self, name = '', health = 0, att = 0, defense = 0):

        self.name = name
        self.health = health
        self.att = att
        self.defense = defense

    def __str__(self):

        return self.name + " has " + str(self.health) + " health, " + str(self.att) + " attack, and " + str(self.defense) + " defense."

    def calculate_damage(self, other):

        d1 = (12 * self.att)/(5 * other.defense) + 2
        rand = random.uniform(0.85, 1)
        damage = d1 * rand
        return damage

    def attack(self, other):

        damage = self.calculate_damage(other)
        if(other.health - damage >= 0):
            other.health = other.health - damage
            other.health = int(round(other.health))
        else:
            other.health = 0

        if(other.health == 0):
            print(other.name + " has fainted")

b = Pokemon('Bulbasaur', 45, 49, 49)
print(b)
c= Pokemon('Charmander', 5, 52, 43)
print(c)
b.attack(c)
print(c)

    
