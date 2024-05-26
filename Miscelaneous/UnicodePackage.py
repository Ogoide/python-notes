'''
The unidecode method in the unidecode module can normalize strings.
That is, special characters are 'translated' into their most common variants.
This useful to remove grammatical accents or convert different alphabets (although not with 100% precision).
This package has to be installed through PyPi, though.
'''

from unidecode import unidecode
print(unidecode('Á'))  # A
print(unidecode('àÁÃâç'))  # aAAac