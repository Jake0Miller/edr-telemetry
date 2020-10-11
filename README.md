# ERD Telemetry

This is a command line program used to create, modify, or delete files. It can also send file data by FTP or HTTP and start processes on the local machine.

## Mode Descriptions

### Create

Allows a user to create a new file, with the user providing the sub-directory structure and filename with extension for specifying file type.

### Modify

Allows a user to modify a file by appending a line at any position, deleting a line, or erasing the entire file.

### Send

Allows a user to send an entire file by FTP or use a file's contents as the body of an HTTP Post request.

### Activate

Allows a user to start a process on the local machine.

## Setup

Built and tested with Python 3.8.5

Create a virtual environment

`python3 -m venv .venv`

## How to Run

Start the program with

`./edr_telemetry -m {mode}`
