#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics for HTTP request logs.

Metrics include:
- Total file size of all requests.
- Counts of specific HTTP status codes
(200, 301, 400, 401, 403, 404, 405, 500).

Prints statistics every 10 lines or upon keyboard interrupt (Ctrl+C) or
end of input (EOF). Lines not matching the expected format are skipped.
"""

import re
import sys


def extract_input(input_line):
    """
    Extracts the status code and file size from a log line.

    Args:
        input_line (str): A line of HTTP request log.

    Returns:
        dict: Contains 'status_code' and 'file_size'.
        Defaults to 0 if not present.
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': '0',
        'file_size': 0,
    }
    log_fmt = f'{fp[0]}-{fp[1]}{fp[2]}{fp[3]}{fp[4]}\\s*'
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    """
    Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): Total accumulated file size.
        status_codes_stats (dict): Dictionary with counts of each status code.
    """
    print(f'File size: {total_file_size}', flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats[status_code]
        if count > 0:
            print(f'{status_code}: {count}', flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """
    Updates the metrics based on a new log line.

    Args:
        line (str): The log line to process.
        total_file_size (int): Current total file size.
        status_codes_stats (dict): Dictionary with current status code counts.

    Returns:
        int: Updated total file size.
    """
    line_info = extract_input(line)
    status_code = line_info['status_code']
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    """
    Starts the log parser, reading from stdin and processing lines.
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line, total_file_size, status_codes_stats
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)
        sys.exit(0)


if __name__ == '__main__':
    run()
