from random import randint
# alternatively, import random
# from ... import ... saves up some memory, whereas import ... results in more readable code

for i in range(0, 5):  # the ending_point of range is the number of iterations in the loop
    # Random.randint(a, b) will generate a pseudo-random integer in the [a,b] interval
    print(randint(0, 10))
