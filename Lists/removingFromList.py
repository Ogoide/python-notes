# It is possible to remove existing values to a list through a variety of ways
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam)
print()

# Method 1 - del statements
# Using a del statement deletes the value with the given index from a list.
# If the given index doesn't exist in the list, an exception is thrown.
# Useful when the index of the item is known.
del spam[1]
print(spam)  # ['hello', 'howdy', 'heyas']

try:
    del spam[10]
except IndexError as e:
    print('IndexError:', e, '\n') # IndexError: list assignment index out of range

# Method 2 - remove() method
# Using the remove() method deletes the given value from a list.
# If the given value doesn't exist in the list, an exception is thrown.
# Useful when the value of the item is known.
spam.remove('howdy')
print(spam)  # ['hello', 'heyas']

try:
    spam.remove('hello there')
except ValueError as e:
    print('ValueError:', e, '\n')  # ValueError: list.remove(x): x not in list

# Method 3 - pop() method
# Using the pop() method removes the last value of a list (index -1) and stores it in a variable for later usage.
# Useful with loops.
pop = spam.pop()
print(spam)  # ['hello']
print(pop)  # heyas