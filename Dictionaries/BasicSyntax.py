# Dictionaries are a MUTABLE collection of many values.
# Indexes can be of varied data types (not just int) and are called 'keys'

# Basic syntax of a dictionary
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# Accessing the values of a dictionary
print(myCat['size'])  # fat
print(f'My cat has {myCat['color']} fur.')  # My cat has gray fur.

# Note that dictionaries can  also use intergers as keys
spam = {12345: 'Luggage Combination', 42: 'The Answer'}
