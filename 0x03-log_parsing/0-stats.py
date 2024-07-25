#!/usr/bin/python3
"""
Parses HTTP request logs from stdin and computes metrics.

Metrics include:
- Total file size of all requests.
- Counts of specific HTTP status codes (200, 301, 400, 401, 403, 404,
  405, 500).

Prints statistics every 10 lines or upon keyboard interrupt (Ctrl+C) or
end of input (EOF). Lines not matching the expected format are skipped.
"""

import re
import sys


def extract_input(input_line):
    """
    Extracts 'status_code' and 'file_size' from a log line.

    Args:
        input_line (str): Log line.

    Returns:
        dict: Contains 'status_code' and 'file_size'.
    """
    log_fmt = (r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>.+?)\] '
               r'"(?P<request>.+?)" (?P<status_code>\d{3}) '
               r'(?P<file_size>\d+)')
    info = {
        'status_code': '0',
        'file_size': 0,
    }
    resp_match = re.match(log_fmt, input_line)
    if resp_match:
        info['status_code'] = resp_match.group('status_code')
        info['file_size'] = int(resp_match.group('file_size'))
    else:
        print(f"Line skipped: {input_line}")
    return info


def print_statistics(total_file_size, status_codes_stats):
    """
    Prints total file size and status code counts.

    Args:
        total_file_size (int): Total file size.
        status_codes_stats (dict): Counts of each status code.
    """
    print(f'File size: {total_file_size}')
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats[status_code]
        if count > 0:
            print(f'{status_code}: {count}')


def update_metrics(line, total_file_size, status_codes_stats):
    """
    Updates metrics with data from a log line.

    Args:
        line (str): Log line.
        total_file_size (int): Current total file size.
        status_codes_stats (dict): Current status code counts.

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
    Reads from stdin, processes lines, and prints metrics.
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
            line = sys.stdin.readline().strip()
            if not line:
                break
            total_file_size = update_metrics(
                line, total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)
        sys.exit(0)


if __name__ == '__main__':
    run()
