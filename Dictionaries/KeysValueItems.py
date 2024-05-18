spam = {'color': 'red', 'age': 42}

# dictionary.keys() creates a dict_keys data type, similar to a list but unchangeable, that can be ued for
# further operations
print(spam.keys())  # dict_keys(['color', 'age'])
# example use-case of dict_keys data type
for k in spam.keys():
    print(k)
    # OUTPUT:
    # color
    # age
print()

# dictionary.values() creates a dict_values data type, referring not to the keys but to the values associated with them
print(spam.values())  # dict_values(['red', 42])
# example use-case of dict_values data type
for v in spam.values():
    print(v)
    # OUTPUT
    # red
    # 42
print()

# dictionary.items() creates a dict_items data type, referring to the key-value pairs
print(spam.items())  # dict_items([('color', 'red'), ('age', 42)])
# example use-case of dict_items data type
for i in spam.items():
    print(i)
    # OUTPUT
    # ('color', 'red')
    # ('age', 42)
print()

# Any of the dict data types can be converted to lists and then iterated over
print(list(spam.keys()))  # ['color', 'age']
print(list(spam.values()))  # ['red', 42]
print(list(spam.items()))  # [('color', 'red'), ('age', 42)]
print()

# This way, the values of these keys, values or items can be accessed by list methods
keys = list(spam.keys())
print(keys[0])  # color
values = list(spam.values())
print(values[0])  # red
items = list(spam.items())
print(items[0])  # ('color', 'red')
print()

# Note that the values of the tuples in the items list can be accessed in the following manner
print(f'Key: {items[0][0]}; Value: {items[0][1]}')  # Key: color; Value: red
# Alternatively, the multiple assignement trick can be used with a for loop
for k, v in spam.items():
    print(f'Key: {k}; Value: {v}')
    # OUTPUT
    # Key: color; Value: red
    # Key: age; Value: 42

