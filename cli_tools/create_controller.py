import os

FILES_DIR = os.getcwd() + '/files'

def go_to(choice):
    globals()[choice]()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_dir(path):
    if not os.path.exists(path): os.makedirs(path)

def create_file(path):
    full_path = FILES_DIR + path
    if os.path.exists(full_path):
        clear_screen()
        print("This file already exists!")
        menu()
    else:
        create_dir('/'.join(full_path.split('/')[0:-1]))
        open('files/' + path, 'w').close()
        clear_screen()
        print('File successfully created. Goodbye.')

def menu():
    options = ['exit', 'view', 'create']
    choice = None

    while choice not in options:
        clear_screen()
        print('Welcome to Create Mode!\n')
        print('Menu options:')
        print('\tView directory contents')
        print('\tCreate a new file\n')
        print('Please select View or Create. Type Exit to quit.\n')
        choice = input().lower()

    go_to(choice)

def view():
    options = ['menu', 'exit']
    choice = None

    while choice not in options:
        clear_screen()
        print('Contents of files directory:\n')

        create_dir(FILES_DIR)

        depth = 0
        for path, subdirs, files in os.walk(FILES_DIR):
            print('-' * depth + path.split('/')[-1] + '/')
            depth += 1
            for file in files:
                print('-' * depth + file)

        choice = input('\nType Menu or Exit: ')

    go_to(choice)

def create():
    clear_screen()
    print('Enter the path and name of a file to create')
    print('  (eg /path/to/my/file.txt)\n')
    print('or type Menu to go back or Exit to quit.\n')
    choice = input().lower()

    if choice in ['menu', 'exit']:
        go_to(choice)
    else:
        create_file(choice)

def exit():
    clear_screen()
    print('Goodbye!')
