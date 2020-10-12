import os

from cli_tools import helpers

FILES_DIR = os.getcwd() + '/files'

def go_to(choice):
    globals()[choice]()

def write_file(path):
    helpers.clear_screen()

def menu():
    options = ['exit', 'view', 'write', 'erase']
    choice = None

    while choice not in options:
        helpers.clear_screen()
        print('Welcome to Modify Mode!\n')
        print('Menu options:')
        print('\tView directory contents')
        print('\tWrite to a file')
        print('\tErase from a file\n')
        print('Please select View, Write, or Erase. Type Exit to quit.\n')
        choice = input().lower()

    go_to(choice)

def view():
    options = ['menu', 'exit']
    choice = None

    while choice not in options:
        helpers.print_directory(FILES_DIR)
        choice = input('\nType Menu or Exit: ')

    go_to(choice)

def write():
    helpers.clear_screen()
    print('Enter the path and name of a file to write to')
    print('  (eg path/to/my/file.txt)\n')
    print('or type Menu to go back or Exit to quit.\n')
    choice = '/' + input().lower()

    if choice in ['menu', 'exit']:
        go_to(choice)
    else:
        write_file(choice)

def exit():
    helpers.clear_screen()
    print('Goodbye!')
