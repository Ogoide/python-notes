# Some data types, like lists, are mutable, meaning you can change thier values
numbers = [0, 1, 2, 3]
numbers[0] = 10
print(numbers, '\n')  # [10, 1, 2, 3]

# Others are immutable, like strings and tuples, meaning you CAN'T change their values
number = '19 is great!'
try:
    number[0] = 2
except  TypeError as e:
    print(f'TypeError: {e}\n')

# To 'change' a string, you can use slicing to create a new 'copy' and change it.
numberv2 = number[:3] + 'is not' + number[5:]
print(numberv2)  # 19 is not great!