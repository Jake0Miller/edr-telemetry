import os

from cli_tools import helpers

FILES_DIR = os.getcwd() + '/files'

def go_to(choice):
    globals()[choice]()

def create_file(path):
    helpers.clear_screen()
    full_path = FILES_DIR + path
    if os.path.exists(full_path):
        print("This file already exists!")
        menu()
    else:
        helpers.create_dir('/'.join(full_path.split('/')[0:-1]))
        open('files/' + path, 'w').close()
        print('File successfully created. Goodbye.')

def menu():
    options = ['exit', 'view', 'create']
    choice = None

    while choice not in options:
        helpers.clear_screen()
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
        helpers.print_directory(FILES_DIR)
        choice = input('\nType Menu or Exit: ')

    go_to(choice)

def create():
    helpers.clear_screen()
    print('Enter the path and name of a file to create')
    print('  (eg path/to/my/file.txt)\n')
    print('or type Menu to go back or Exit to quit.\n')
    choice = '/' + input().lower()

    if choice in ['menu', 'exit']:
        go_to(choice)
    else:
        create_file(choice)

def exit():
    helpers.clear_screen()
    print('Goodbye!')
