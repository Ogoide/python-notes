# Oftentimes, there is the need to assign a new value to a key ONLY if that key doesn't already exist
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:  # check if key 'color' exists in spam.
    spam['color'] = 'black'  # if it doesn't, create it and assign the value 'black' to it
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

# The setdefault() method serves as a shortcut, enabling this operation in a single line of code.
# It takes two arguments: the name of the key to check for and to create and the value to assign to it.
eggs = {'name': 'Pooka', 'age': 5}
eggs.setdefault('color', 'black')  # Creates a 'color' key and assigns the value 'black'
eggs.setdefault('name', 'Mariah')  # Doesn't do anything, as this key already exists
print(eggs)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}
