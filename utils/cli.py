import argparse

def command_line_arguments():
    parser = argparse.ArgumentParser(
        description =
        '''\tCLI for manipulating files and sending data.\n
        Add a JSON file to /playbooks (see test files for examples)
        Then run the program ./edr_telemetry -f example.json''',
        formatter_class = argparse.RawTextHelpFormatter
    )

    group = parser.add_argument_group(
        title = 'required',
        description = '-f, --file filename.json'
    )

    group.add_argument(
        '-f', '--file',
        dest='file',
        action = 'store',
        metavar = '',
        required = True,
        help = argparse.SUPPRESS
    )

    return parser.parse_args()
