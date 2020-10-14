from utils import create_controller as cc
from utils import modify_controller as mc
from utils import delete_controller as dc
from utils import udp_controller as uc
from utils import run_controller as rc

def create(action, source):
    path, filename = action['path'], action['filename']
    cc.create_file(path, filename, source)

def delete(action, source):
    path, filename = action['path'], action['filename']
    dc.delete_file(path, filename, source)

def append(action, source):
    path, filename = action['path'], action['filename']
    line = action['line']
    mc.append(path, filename, line, source)

def erase(action, source):
    path, filename = action['path'], action['filename']
    mc.erase(path, filename, source)

def send(action, source):
    destination = action['destination']
    destination = (destination['address'], int(destination['port']))
    port = action['source']['port']
    data = action['data']
    uc.send(destination, port, data, source)

def run(action, source):
    process, arguments = action['process'], action['arguments']
    rc.run(process, arguments)
