import os

def print_directory(files_dir):
    clear_screen()
    print('Contents of files directory:\n')
    create_dir(files_dir)
    for path, subdirs, files in os.walk(files_dir):
        for file in files:
            print(path.split('edr-telemetry/files/')[1] + '/' + file)

def create_dir(path):
    if not os.path.exists(path): os.makedirs(path)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
