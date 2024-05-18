class Dog:
    # pass - pass is a keyword used as a placeholder for future code or information
    # Class attributes- values globally equal to all instances of the class - defined outside of __init__
    species = "Canis familiaris"

    def __init__(self, name, age):  # Initializes the initial state of class instances/objects
        # Instance attributes - values unique to each instance, initialized upon its creation - defined within __init__
        self.name = name
        self.age = age

# Instantiating a new Dog object
miles = Dog('Miles', 4)
buddy = Dog('Buddy', 2)
print(miles)  # <__main__.Dog object at 0x0000021D6AF6E7E0> - memory address
print(buddy)  # <__main__.Dog object at 0x0000021D6AF6E810>
print()

# Exception thrown with insufficient parameters
try:
    dog = Dog()
except TypeError as e:
    print('TypeError: ', e)  # TypeError:  Dog.__init__() missing 2 required positional arguments: 'name' and 'age'

# Accessing class and instance attributes
print(miles.name)  # Miles
print(miles.age)  # 4
print(buddy.name)  # Buddy
print(buddy.age)  # 2
print(miles.species)  # Canis familiaris
print(buddy.species)  # Canis familiaris

# Changing attributes' values
miles.age = 10
miles.species = 'Canis Lupus'
print(miles.age)  # 10
print(miles.species)  # Canis Lupus
# Despite class attributes being globally equal to all objects upon instantiation, if said values are changed after
# that point, these changes only apply to the changed object
print(buddy.species)  # Canis familiaris 



