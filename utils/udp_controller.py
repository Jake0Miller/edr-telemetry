import socket

from utils import logger

def send(destination, port, data, source):
    encoded_data = data.encode('utf-8')
    amount = len(encoded_data)
    protocol = 'udp'

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    host = socket.gethostbyname(socket.gethostname())
    s.bind((host, int(port)))
    s.sendto(encoded_data, destination)

    logger.log_send(destination, port, host, amount, protocol, source)
