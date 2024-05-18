birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input('Enter a name (blank to quit):\n')
    if name.strip() == '':
        break
    if name in birthdays:
        print(f'The birthday of {name} is {birthdays[name]}.')
    else:
        print(f'I do not have brithday information for {name}.')
        new_birthday = input('What is their birthday?\n')
        # Assigning a new value to a dictionary (there is no need for fancy methods such as append), only for a key
        # and the corresponding value
        birthdays[name] = new_birthday
        print('Birthdays database updated!')

