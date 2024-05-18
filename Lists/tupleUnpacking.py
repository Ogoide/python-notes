cat = ['fat', 'gray', 'loud']

# The multiple assignment trick (technically called tuple unpacking) is a shortcut
# that lets you assign multiple variables with the values in a list in one line of code.

# Instead of doing:
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# It is possible to simply do this:
size, color, disposition = cat
print(size, color, disposition)  # fat gray loud
# However, the number of variables and values to assign must be the same, otherwise Pyhon will throw a ValueError
# exception

