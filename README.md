# ERD Telemetry

This program can create, modify, and delete files. It can open a connection and send data and also run processes on the local machine.

## Setup

Built and tested with Python 3.8.5

Create a virtual environment

`python3 -m venv .venv`

## Usage

Start the program with

`./edr_telemetry -f {file}`

Place JSON files in `/playbooks` and select which file you would like to run.

See `setup_test.json`, `modify_test.json`, `teardown_test.json` etc for examples. Run these files to see how the program works.

## Action Descriptions

### Create

Create a new file with the provided the path and filename.

### Append

Append a line to the end of a file. Requires a path and filename as well as the line to be appended.

### Delete

Delete a file, with the user providing the path and filename.

### Send



### Activate


## Dependencies

Python module `requests`

Install via `pip install requests`
