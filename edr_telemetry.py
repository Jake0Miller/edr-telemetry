#!.venv/bin/python

from cli_tools import cli

if __name__ == "__main__":
    args = cli.command_line_arguments()
    mode = args.mode
    getattr(cli, mode)()
