# Tuples are an array of items very similar to lists, supporting most lists' functions
# the main differences are:
    # Tuples are written with curved parentheses '()'
    # Tuples are immutable, not supporting this such as assignement, append(), remove(), among others

tup = ('hello', 42, 0.5)
print(tup[0])  # hello

try:
    # noinspection PyTupleItemAssignment
    tup[0] = 'goodbye'
except TypeError as e:
    print(f'TypeError: {e}')  # TypeError: 'tuple' object does not support item assignment

# If a tuple only has one value, use a trailing comma to indicate it's one
print(type(('goodbye')))  # <class 'str'>
print(type(('goodbye',)))  # <class 'tuple'>
print()

# ---CONVERTING LISTS AND TUPLES---
animals = ['cat', 'dog', 'rhino']
print(type(animals))  # <class 'list'>
animals2 = tuple(animals)
print(animals2, type(animals2))  # ('cat', 'dog', 'rhino') <class 'tuple'>
print()
message = 'hello'
print(list(message))  # ['h', 'e', 'l', 'l', 'o']
print(tuple(message))  # ('h', 'e', 'l', 'l', 'o')
