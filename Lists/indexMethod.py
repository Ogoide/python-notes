# list.index(value) return the index of the given value in the given list
# this method will throw an exception if the given value is not present in the list
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('howdy')) # 2

try:
    spam.index('hello there')
except Exception as e:
    print(e) # 'hello there' is not in list

# NOTE: if the same value appears multiple times in the given list, only the index of its first iteration will be
# returned
