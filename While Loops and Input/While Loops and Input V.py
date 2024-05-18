# Using while loops to process items in a list (exit() exits a program!!)

# Start with a list of unconfirmed users, and an empty list of confirmed users.
unconfirmed_users = ['ada', 'billy', 'clarence', 'daria']
confirmed_users = []

# Work through the list, and confirm each user.
while len(unconfirmed_users) > 0:
    # Get the latest unconfirmed user, and process them.
    current_user = unconfirmed_users.pop(0)
    print("Confirming user %s...confirmed!" % current_user.title())

    # Move the current user to the list of confirmed users.
    confirmed_users.append(current_user)

# Prove that we have finished confirming all users.
print("\nUnconfirmed users:")
for user in unconfirmed_users:
    print('- ' + user.title())

print("\nConfirmed users:")
for user in confirmed_users:
    print('- ' + user.title())