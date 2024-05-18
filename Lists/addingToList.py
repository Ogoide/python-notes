# It is possible to add new values to a list through a variety of ways
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam)

# Method 1 - concatenation
spam += ['hello there']
print(spam) # ['hello', 'hi', 'howdy', 'heyas', 'hello there']

# Method 2 - append() method
# This method adds the given value to the end of the given list, equivalent to list.insert(-1, value)
spam.append('good morning')
print(spam) # ['hello', 'hi', 'howdy', 'heyas', 'hello there', 'good morning']

# Method 3 - insert() method

# This method adds the given value to the specified index of the given list, displacing the remaining values
spam.insert(1, 'Salutations')
print(spam)  # ['hello', 'Salutations', 'hi', 'howdy', 'heyas', 'hello there', 'good morning']
