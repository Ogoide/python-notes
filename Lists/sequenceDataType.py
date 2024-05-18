# Sequence Data Type refers to objects that represent an order of other objects
# These can be lists, strings, range objects returned by range() and tuples
# List methods and functions are common to the sequence data type
string = 'hello'

print(string[0])  # h
print(string[-1])  # o
print(string[:])  # hello
print(string[2:])  # llo
print(string[:-1])  # hell
print()

print('h' in string)  # True
print('z' not in string)  # True
print('z' in string)  # False
print('h' not in string)  # False
print()

print(string.index('h'))  # 0
print()

for i in string:
    print(i)

# OUTPUT
# h
# e
# l
# l
# o
