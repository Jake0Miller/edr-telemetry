import os

def print_directory(files_dir):
    print('Contents of files directory:\n')
    depth = 0
    for path, subdirs, files in os.walk(files_dir):
        print('-' * depth + path.split('/')[-1] + '/')
        depth += 1
        for file in files:
            print('-' * depth + file)
