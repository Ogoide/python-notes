def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: # It is possible to specify which error to catch (or not)
        return 'Not possible to divide by zero.'

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))