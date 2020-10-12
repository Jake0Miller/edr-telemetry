import os

FILES_DIR = os.getcwd() + '/files'

def prune_subdirectories():
    locs = []
    for path, subdirs, files in os.walk(FILES_DIR):
        for subdir in subdirs:
            base = path.split('edr-telemetry/')
            loc = base[1] + '/' + subdir
            locs.insert(0, loc)
            if not os.listdir(loc):
                os.rmdir(loc)
    for loc in locs:
        if os.path.exists(loc) and not os.listdir(loc):
            os.rmdir(loc)

def delete_file(path, filename):
    if path[0] != '/':
        path = '/' + path

    full_path = FILES_DIR + path + filename

    if os.path.exists(full_path):
        os.remove(full_path)
        print('File successfully deleted.')
        prune_subdirectories()
    else:
        print("This file does not exist!")