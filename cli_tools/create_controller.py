import os

def go_to(choice):
    globals()[choice]()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    options = ['exit', 'path', 'contents', 'create']
    choice = None

    while choice not in options:
        clear_screen()
        print('Welcome to Create Mode!\n')
        print('Menu options:')
        print('\tShow current working directory path')
        print('\tView contents of current working directory')
        print('\tCreate a file relative to current working directory\n')
        print('Please select Path, Contents, or Create. Type Exit to quit.\n')
        choice = input().lower()

    go_to(choice)

def path():
    options = ['menu', 'exit']
    choice = None

    while choice not in options:
        clear_screen()
        print('Current directory: ' + os.getcwd() + '\n')
        choice = input('Type Menu or Exit: ')

    go_to(choice)

def contents():
    options = ['menu', 'exit']
    choice = None

    while choice not in options:
        clear_screen()
        print('Contents of current directory:\n')
        contents = os.listdir()
        for item in contents:
            if item[0] != '.': print(item)

        choice = input('\nType Menu or Exit: ')

    go_to(choice)

def create():
    print('End of progress')

def exit():
    clear_screen()
    print('Goodbye!')
