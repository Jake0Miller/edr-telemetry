import os

from cli_tools import helpers

FILES_DIR = os.getcwd() + '/files'

def go_to(choice):
    globals()[choice]()

def prune_subdirectories():
    for path, subdirs, files in os.walk(FILES_DIR):
        for subdir in subdirs:
            base = path.split('edr-telemetry/')
            loc = base[1] + '/' + subdir
            if not os.listdir(loc):
                os.rmdir(loc)

def delete_file(path):
    helpers.clear_screen()
    full_path = FILES_DIR + path
    print(full_path)
    if os.path.exists(full_path):
        os.remove(full_path)
        print('File successfully deleted. Goodbye.')
        prune_subdirectories()
    else:
        print("This file does not exist!")
        import pdb; pdb.set_trace()
        menu()

def menu():
    options = ['exit', 'view', 'delete']
    choice = None

    while choice not in options:
        helpers.clear_screen()
        print('Welcome to Delete Mode!\n')
        print('Menu options:')
        print('\tView directory contents')
        print('\tDelete a file\n')
        print('Please select View or Delete. Type Exit to quit.\n')
        choice = input().lower()

    go_to(choice)

def view():
    options = ['menu', 'exit']
    choice = None

    while choice not in options:
        helpers.print_directory(FILES_DIR)
        choice = input('\nType Menu or Exit: ')

    go_to(choice)

def delete():
    helpers.clear_screen()
    print('Enter the path and name of a file to delete')
    print('  (eg path/to/my/file.txt)\n')
    print('or type Menu to go back or Exit to quit.\n')
    choice = '/' + input().lower()

    if choice in ['menu', 'exit']:
        go_to(choice)
    else:
        delete_file(choice)

def exit():
    helpers.clear_screen()
    print('Goodbye!')
