# On each iteration of the loop, enumerate() will return two values: the index of the item in the list, and the item
# in the list itself.
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# Enumerate syntax:
for index, item in enumerate(supplies):
    print(f'Index {index} in supplies is: {item}.')

# The enumerate() function is useful if both the item and the item’s index are needed.

# OUTPUT
# Index 0 in supplies is: pens.
# Index 1 in supplies is: staplers.
# Index 2 in supplies is: flamethrowers.
# Index 3 in supplies is: binders.