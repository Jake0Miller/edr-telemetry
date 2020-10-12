import json

from utils import process_controller as pc

def process(file):
    with open(file) as f:
        data = json.load(f)

    for action in data['actions']:
        getattr(pc, action['method'])(action)
