# It is possible to check wether a value exists in a spam using the in and not keywords
spam = {'name': 'Zophie', 'age': 7}

# Checking keys
print('name' in spam.keys())  # True
print('age' in spam.keys())  # True
print('name' not in spam.keys())  # False
print('eggs' in spam.keys())  # False
print()
# Alternatively, to check EXCLUSIVELY keys, the added method is not needed, and the dictionary's name can be used
# directly.
print('name' in spam)  # True
print('age' in spam)  # True
print('name' not in spam)  # False
print('eggs' in spam)  # False
print()

# Checking values
print('Zophie' in spam)  # False - using simply 'spam' checks keys and not values
print('Zophie' in spam.values())  # True
print(7 in spam.values())  # True
print('Zophie' not in spam.values())  # False
print(42 in spam.values())  # False
print()

# Checking items
print(('name', 'Zophie') in spam.items())  # True
print(('age', 7) in spam.items())  # True
print(('name', 7) in spam.items())  # False
# and so on, and so on...
