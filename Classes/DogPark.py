# Example of use-cases of class inheritance
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # NOTE: changes to parent class automatically apply
    def speak(self, sound):
        print(f"{self.name} says {sound}.\n")


# Creating different child classes to specific dog breeds, as their bark sound varies
class JackRussellTerrier(Dog):
    # Overriding speak method from Parent class
    def speak(self, sound='Arf!'):
        # call super().speak(sound) inside JackRussellTerrier, Python searches the parent class, Dog, for a .speak()
        # method and calls it with the variable sound super() traverses the entire class hierarchy in search of a
        # method with the same name, so it can produce unexpected results if used without care
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


# Instantiating Dog objects of different breeds (different Child classes)
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# Objects of Child class inherit attributes and methods of Parent class
print(miles.species)  # Canis familiaris
print(buddy.species)  # Canis familiaris
print(jack.species)  # Canis familiaris
print(jim.species, '\n')  # Canis familiaris

print(miles.age)  # 4
print(buddy.name)  # Buddy
print(jack)  # Jack is 3 years old
jim.speak('woof')  # Jim says woof

# Determining a class of a specific object
print(type(miles))  # <class '__main__.JackRussellTerrier'>

# Determining if an object is an instance of a specific class
print(isinstance(miles, JackRussellTerrier))  # True
print(isinstance(miles, Bulldog), '\n')  # False

# Using the overridden method of Child class
miles.speak()  # Miles says Arf
