# the global statement can be used inside a function to change a global variable, outside the function's local scope

def spam():
    global eggs  # since egg is declared to be global, all calls to it afterward change the global variable
    eggs = 'spam'


eggs = 'global'
print(eggs)
spam()  # function with global statement changes
print(eggs)
