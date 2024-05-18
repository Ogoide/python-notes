def function(list1):  # Copies the reference (id) to the numbers list for the function
    eggs = list1  # Copies the reference to the passed list to a new variable, referencing the same list value
    eggs.append(4)  # Changes the original list value, now referenced by both eggs AND numbers

numbers = [0,1,2,3]
function(numbers)
print(numbers)  # Because the list value was never actually copied, changing the list value via append() in the eggs
# variable is changing the ORIGINAL value of the list, which is then referenced by two SEPARATE variables
# this changes not only the value stored in eggs but also in numbers, as these variables reference the same value
