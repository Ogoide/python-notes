supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    # This technique iterates through every list value using their indexes, useful to retrieve items' indexes.
    # Alternatively,the standard "for supply in supplies" should works, although not returning the index values.
    print(f'Index {i} in supplies is: {supplies[i]}.')

# OUTPUT
# Index 0 in supplies is: pens.
# Index 1 in supplies is: staplers.
# Index 2 in supplies is: flamethrowers.
# Index 3 in supplies is: binders.