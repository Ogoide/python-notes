# The get() method uses a key's name and a fallback value.
# If that key exists in the dictionary the method is called on, get() returns the value associated with that key.
# If the key does not exist, it returns the fallback value.
spam = {'name': 'Zophie', 'age': 7}

# get() syntax
print(spam.get('name','name does not exist'))  # Zophie
print(spam.get('height', 'height does not exist'))  # height does not exist

# Example use of get()
print(f'This person is called {spam.get('name', 'huh?')} and is {spam.get('age', 'who knows how many')} years old.')
# This person is called Zophie and is 7 years old.
print(f'This person is called {spam.get('ame', 'huh?')} and is {spam.get('ge', 'who knows how many')} years old.')
# This person is called huh? and is who knows how many years old.
