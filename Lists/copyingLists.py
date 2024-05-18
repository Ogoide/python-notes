# If you want to change the original list (or dictionary) values, the best method is not to copy the
# reference (eggs = spam), since any change to either variable will affect the other, but to copy the
# value itself.

# Method 1: slicing
list1 = [0,1,2,3]
list2 = list1[:]  # Copying the list value
print(list2)  # [0, 1, 2, 3]
list2.append(22)
print(list1, ';', list2, '\n')  # [0, 1, 2, 3] ; [0, 1, 2, 3, 22] - list1 is not changed with list2

# Method 2: Copy Module
import copy

# Method 2.1: copy.copy() method
list3 = copy.copy(list1) # Copying ultimately creates a new value in the memory with the exact contents,
list3.append(33)         # thus resulting in variables with the same values but diiferent references (IDs)
print(list1, ';', list3, '\n')  # [0, 1, 2, 3] ; [0, 1, 2, 3, 33]

# Method 2.2: copy.deepcopy()
# This method's only difference is that it copies lists within lists as well



