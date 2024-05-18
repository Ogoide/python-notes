# It is possible to get a random value from a list via a variety of methods.
import random

pets = ['Dog', 'Cat', 'Moose']

# Method 1 - The long way
pet1 = pets[random.randint(0, len(pets) - 1)]  # NOTE: len(pets) return 3 but the highest index is 2
print(pet1)

# Method 2 - The straight way
pet2 = random.choice(pets)  # random.choice(pets) returns a random value present in the pets list
print(pet2)

# Method 3 - The roundabout way
print()
print(pets)
random.shuffle(pets)  # ramdom.shuffle(pets) simply randomizes the order of the values in the pets list
print(pets)  # From here, even calling the same index will return a random value, as the value in that index is
# constantly changed.
