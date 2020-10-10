import argparse
import os

from cli_tools import create_controller

def command_line_arguments():
    parser = argparse.ArgumentParser(
        description =
        '''\tCLI for manipulating files and sending data.\n
        Mode descriptions:
            create a new file
            write to an existing file
            erase the last line of a file
            clear a file's contents completely
            delete a file entirely
            send a file by FTP use its contents for an HTTP body
            activate a process''',
        formatter_class = argparse.RawTextHelpFormatter
    )

    group = parser.add_argument_group(
        title = 'required',
        description = '-m, --mode  {create,write,erase,clear,delete,send,activate}'
    )

    group.add_argument(
        '-m', '--mode',
        dest='mode',
        action = 'store',
        metavar = '',
        choices = ['create', 'write', 'erase', 'clear', 'delete', 'send', 'activate'],
        required = True,
        help = argparse.SUPPRESS
    )

    return parser.parse_args()

def create():
    create_controller.menu()
