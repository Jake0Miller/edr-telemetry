#!.venv/bin/python

from utils import cli
from utils import json_processor as jp

if __name__ == "__main__":
    args = cli.command_line_arguments()
    jp.process(args.file)
