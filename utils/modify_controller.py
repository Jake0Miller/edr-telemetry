import os

from utils import logger

FILES_DIR = os.getcwd() + '/files'

def append(path, filename, line, source):
    if path[0] != '/':
        path = '/' + path

    full_path = FILES_DIR + path + filename

    if os.path.exists(full_path):
        with open('files' + path + filename, 'a') as f:
            f.write(line)
        logger.log_file(full_path, 'append', source)
    else:
        print("This file does not exist!")

def erase(path, filename, source):
    if path[0] != '/':
        path = '/' + path

    full_path = FILES_DIR + path + filename

    if os.path.exists(full_path):
        open(full_path, 'w').close()
        logger.log_file(full_path, 'erase', source)
    else:
        print("This file does not exist!")
