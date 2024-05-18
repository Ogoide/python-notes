message = 'howdy!'
print(id(message),'\n')

# When Python runs id('howdy!'), it creates the 'howdy!' string in the computer’s memory. The numeric memory address
# where the string is stored is returned by the id() function. Python picks this address based on which memory bytes
# happen to be free on the computer at the time, so it’ll be different each time you run this code.

# When 'changing' an immutable data type like 'str' or 'int', instead of the value referenced by the variable changing,
# a new one is simply created and referenced by that variable, thus resulting in a different memory id

bacon = 'Hello'
print(id(bacon))
bacon += ' World!'  # 'Hello World!'
print(id(bacon), '\n')

# However, when modifying mutable data types in place, the id is kept the same, as the actual value is changed,
# as opposed to just its reference.

eggs = ['cat', 'rat']
print(id(eggs))
eggs.append('bat')
print(id(eggs))
eggs.sort()
print(id(eggs))

# Python’s automatic garbage collector deletes any values not being referred to by any variables to free up memory
