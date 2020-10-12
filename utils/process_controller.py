from utils import create_controller as cc
from utils import modify_controller as mc
from utils import delete_controller as dc

def create(action):
    path, filename = action['path'], action['filename']
    cc.create_file(path, filename)

def delete(action):
    path, filename = action['path'], action['filename']
    dc.delete_file(path, filename)

def append(action):
    path, filename = action['path'], action['filename']
    line = action['line']
    mc.append(path, filename, line)

def erase(action):
    path, filename = action['path'], action['filename']
    mc.erase(path, filename)
