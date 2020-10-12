import os

FILES_DIR = os.getcwd() + '/files'

def create_file(path, filename):
    if path[0] != '/':
        path = '/' + path

    full_path = FILES_DIR + path + filename

    if os.path.exists(full_path):
        print("This file already exists!")
    else:
        if not os.path.exists(FILES_DIR + path):
            os.makedirs(FILES_DIR + path)
        open('files' + path + filename, 'w').close()
        print('File successfully created.')
