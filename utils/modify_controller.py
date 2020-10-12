import os

FILES_DIR = os.getcwd() + '/files'

def append(path, filename, line):
    if path[0] != '/':
        path = '/' + path

    full_path = FILES_DIR + path + filename

    if os.path.exists(full_path):
        with open('files' + path + filename, 'a') as f:
            f.write(line)
        print('Line appended to file.')
    else:
        print("This file does not exist!")

def erase(path, filename):
    if path[0] != '/':
        path = '/' + path

    full_path = FILES_DIR + path + filename

    if os.path.exists(full_path):
        open(full_path, 'w').close()
        print('File emptied.')
    else:
        print("This file does not exist!")
