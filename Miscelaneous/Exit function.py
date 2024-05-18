import sys

while True:
    print('Type \"exit\" to exit.')
    response = input()
    if response.lower().strip() == 'exit':
        # sys.exit() straightforwardly terminates the program prematurely
        sys.exit()
    print('You typed ' + response + '.')
