import os

from utils import logger

FILES_DIR = os.getcwd() + '/files'

def prune_subdirectories():
    locs = []
    for path, subdirs, files in os.walk(FILES_DIR):
        for subdir in subdirs:
            dir_name = os.getcwd().split('/')[-1]
            base = path.split(dir_name + '/')[-1]
            loc = base + '/' + subdir
            locs.insert(0, loc)
            if not os.listdir(loc):
                os.rmdir(loc)
    for loc in locs:
        if os.path.exists(loc) and not os.listdir(loc):
            os.rmdir(loc)

def delete_file(path, filename, source):
    if path[0] != '/':
        path = '/' + path

    full_path = FILES_DIR + path + filename

    if os.path.exists(full_path):
        os.remove(full_path)
        logger.log_file(full_path, 'delete', source)
        prune_subdirectories()
    else:
        print("This file does not exist!")
