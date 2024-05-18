# the sort() method sorts list either numerically or alphabetically
numspam = [2, 5, 3.14, 1, -7]
print(numspam)
numspam.sort()
print(numspam, '\n')  # [-7, 1, 2, 3.14, 5]

animalspam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(animalspam)
animalspam.sort()
print(animalspam, '\n')  # ['ants', 'badgers', 'cats', 'dogs', 'elephants']

# sort() can't be used in with lists that have both int and str values, resulting in a TypeError exception
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants', 2, 5, 3.14, 1, -7]
try:
    spam.sort()
except TypeError as e:
    print('TypeError:', e, '\n')  # TypeError: '<' not supported between instances of 'int' and 'str'

# Additionly, by passing the keyword argument reverse=True, the list is sorted in the reversed order.
numspam = [2, 5, 3.14, 1, -7]
print(numspam)
numspam.sort(reverse=True)
print(numspam, '\n')  # [5, 3.14, 2, 1, -7]

animalspam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(animalspam)
animalspam.sort(reverse=True)
print(animalspam, '\n')  # ['elephants', 'dogs', 'cats', 'badgers', 'ants']

# Moreover, sort() uses “ASCIIbetical order”, which means uppercase letters come before lowercase ones.
# To perform true sorting, key=str.lower can be passed, so that values are analyzed as if they were lowercase
asciispam = ['a', 'z', 'A', 'Z']
print(asciispam)
asciispam.sort()
print(asciispam)  # ['A', 'Z', 'a', 'z']
asciispam.sort(key=str.lower)
print(asciispam)  # ['A', 'a', 'Z', 'z']
