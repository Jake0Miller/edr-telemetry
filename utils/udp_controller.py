import socket

from utils import logger

def send(destination, port, data, source):
    encoded_data = data.encode('utf-8')
    amount = len(encoded_data)
    protocol = 'udp'

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        host = socket.gethostbyname(socket.gethostname())
        s.bind(('', int(port)))
        s.sendto(encoded_data, destination)

        logger.log_send(destination, port, host, amount, protocol, source)
    except:
        print('Error encountered when sending UDP packet')
