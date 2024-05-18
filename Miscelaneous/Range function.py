# range(starting_point, stopping_point)
print(list(range(0, 5)), "\n")  # [0, 1, 2, 3, 4]

# the range function creates a list of numbers starting from starting_point
# until (stopping_point - 1)

# the third argument is the steps. steps: 1 makes range count from one in one; 2 from two to two, etc
# negative steps makes it count backwards
print("Steps: 1")
print(list(range(0, 11, 1)))
print("Steps: 2")
print(list(range(0, 11, 2)))
print("Steps: 3")
print(list(range(0, 11, 3)))
print("Steps: -1")
print(list(range(10, -1, -1)), "\n") # When using negative steps, starting_point and ending_point are reversed

# range makes it easier to properly use loops as well as getting list of multiples of a certain number
print("Multiples of 7 smaller than 100:")
print(list(range(0, 101, 7)))
print("Multiples of 3.25 smaller than 100:")
ttfmults = []
for i in range(0, 101):
    num = i * 3.2
    if num < 100:
        ttfmults.append(round(num, 1))
print(ttfmults)
