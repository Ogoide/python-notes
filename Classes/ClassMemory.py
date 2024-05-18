# OBJECTS OF THE SAME CLASS ARE STORED AT DIFFERENT MEMORY ADDRESSES, EVEN IF THE CLASS' ATTRIBUTES ARE THE SAME

# Defining a class
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Dog('name', 'age')
b = Dog('name', 'age')

# The values of a and b's attributes are the same
print(a.species == b.species)  # True
print(a.age == b.age)  # True
print(a.name == b.name)  # True

# Objects themselves are different
print(a == b)  # False
