message = 'It was a bright cold day in April, and the clocks were striking thirteen'
char_count = {}

# Checks each character in message against the char_count dictionary.
# If that specific character is as yet to be recorded in the dictionary, record it.
# If it has, add one to the it's count
for char in message:
    char_count.setdefault(char, 0)  # If the key corresponding to the character doesn't exist, create it and assign
    # the count of 0
    char_count[char] += 1  # For each character checked, add one to its count if it it checked
print(char_count)