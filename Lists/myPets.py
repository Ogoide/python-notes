myPets = ['Zophie', 'Pooka', 'Fat-tail']
pet_name = input('Enter a pet name.\n')

if pet_name not in myPets:
    print(f'I don\'t have a pet named {pet_name}')
else:
    print(f'{pet_name} is my pet.')
