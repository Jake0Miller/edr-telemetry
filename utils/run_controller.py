import subprocess

from utils import logger

def run(process, arguments):
    arguments.insert(0, process)
    proc = subprocess.Popen(arguments)
    logger.log_run(process, arguments, proc.pid)
