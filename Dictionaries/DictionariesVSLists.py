# Unlike lists, values in a dictionary are unordered. While the first item in a list would be list[0],
# there is no such thing as dictionary[0] (unless the int value 0 is a key)
# Therefore, while the values' order matters to differentiate lists, it does not when it comes to dictionaries

list1 = ['cats', 'dogs', 'moose']
list2 = ['dogs', 'moose', 'cats']
print(list1 == list2)  # False - the lists are different

dictionary1 = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
dictionary2 = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(dictionary1 == dictionary2)  # True - the dictionaries are the same

# Because dictionaries are unordered, it is impossible to slice them as list and a non-existing key will result im
# a KeyError
person = {'name': 'Zophie', 'age': 7}
try:
    print(person['gender'])
except KeyError as k:
    print('KeyError:', k)  # KeyError: 'gender'
