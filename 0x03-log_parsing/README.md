# Log Parsing Metrics Script

## Description

This project consists of a Python script that reads logs from the standard input line by line, computes metrics based on the log content, and prints statistics periodically or upon keyboard interruption. The logs follow a specific format, and the script calculates the total file size and counts the occurrences of specific HTTP status codes.

## Input Format

The expected log input format is as follows:

`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

- **IP Address:** The IP address of the client.
- **date:** The date and time when the request was made.
- **status code:** The HTTP status code returned by the server.
- **file size:** The size of the requested file in bytes.

If a log entry does not match this format, it will be skipped.

## Features

- Reads logs from standard input line by line.
- Computes the total file size from all log entries.
- Counts the number of occurrences of each HTTP status code.
- Prints statistics after every 10 lines of input.
- Prints statistics upon receiving a keyboard interruption (CTRL + C).

## Usage

### Running the Script

To run the script, use the following command:

```sh
./log_parsing.py
```

### Sample Usage with Log Generator

You can use a log generator script to provide input to the log parsing script:

```sh
./log_generator.py | ./log_parsing.py
```

### Script Output

After every 10 lines or upon keyboard interruption, the script outputs:

### The total file size.

The number of occurrences of each status code (200, 301, 400, 401, 403, 404, 405, 500).

### Example output:

Total file size: File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3

## Handling Interruptions

If the script is interrupted using CTRL + C, it will gracefully print the statistics collected so far and then exit.
