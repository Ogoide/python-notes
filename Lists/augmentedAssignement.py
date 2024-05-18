i = 7
print(i) # 7
print()

# i = i / 2
i /= 2
print(i) # 3.5

i = 7
# i = i * 2
i *= 2
print(i) # 14

i = 7
# i = i % 2
i %= 2
print(i) # 1

i = 7
# i = i // 2 - floor division
i //= 2
print(i) # 3

i = 7
# i = i + 2
i += 2
print(i) # 9

i = 7
# i = i -2
i -= 2
print(i) # 5
print()

# += and *= can also be used to concatenate and replicate lists and strings
list1 = ['value1']
string1 = 'value2'

list1 += ['value3']
print(list1)  # ['value1', 'value3']
list1 *= 2
print(list1)  # ['value1', 'value3', 'value1', 'value3']
print()

string1 += 'value4'
print(string1)  # value2value4
string1 *= 2
print(string1)  # value2value4value2value4
