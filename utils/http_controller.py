import requests

def send(address, data):
    r = requests.post(address, data=data)
    print(r.status_code, r.reason)
