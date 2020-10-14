from datetime import datetime
import getpass
import csv
import os

def make_folder():
    if not os.path.exists('logs'):
        os.makedirs('logs')

def write_csv(file, data, header):
    exists = os.path.exists(file)

    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(header)
        writer.writerow(data)

def log_run(process, command, pid):
    make_folder()
    file = 'logs/run_log.csv'
    header = ['timestamp', 'uid', 'process', 'command', 'pid']

    data = []
    data.append(str(datetime.now())[0:19])
    data.append(getpass.getuser())
    data.append(process)
    data.append(' '.join(command))
    data.append(pid)

    write_csv(file, data, header)

def log_send(destination, port, host, amount, protocol, source):
    make_folder()
    file = 'logs/send_log.csv'
    header = ['timestamp', 'uid', 'dest_address', 'dest_port', 'source_address',
        'source_port', 'amount_of_data', 'protocol', 'process', 'command', 'pid']

    data = []
    data.append(str(datetime.now())[0:19])
    data.append(getpass.getuser())
    data.append(destination[0])
    data.append(destination[1])
    data.append(host)
    data.append(port)
    data.append(amount)
    data.append(protocol)
    data.append('edr_telemetry')
    data.append('./edr_telemetry -f {}'.format(source))
    data.append(os.getpid())

    exists = os.path.exists(file)

    write_csv(file, data, header)

def log_file(path, method, source):
    make_folder()
    file = 'logs/file_log.csv'
    header = ['timestamp', 'path', 'method', 'uid', 'process', 'command', 'pid']

    data = []
    data.append(str(datetime.now())[0:19])
    data.append(path)
    data.append(method)
    data.append(getpass.getuser())
    data.append('edr_telemetry')
    data.append('./edr_telemetry -f {}'.format(source))
    data.append(os.getpid())

    write_csv(file, data, header)
