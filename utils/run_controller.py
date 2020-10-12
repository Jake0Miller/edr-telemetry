import subprocess

def run(process, arguments):
    arguments.insert(0, process)
    subprocess.call(arguments)
