#!/usr/bin/python3
'''A script for parsing HTTP request logs and computing statistics.'''

import re


def extract_request_info(log_line):
    '''Extracts relevant information from a line of HTTP request log.

    Args:
        log_line (str): A line from the HTTP request log.

    Returns:
        dict: Dictionary containing extracted information
        (status_code and file_size).
    '''
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(*log_pattern)
    match = re.fullmatch(log_format, log_line)
    if match:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info


def print_statistics(total_file_size, status_code_counts):
    '''Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): Total file size accumulated.
        status_code_counts (dict): Dictionary containing counts of status codes
    '''
    print('Total file size:', total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        print(status_code, ':', count)


def update_metrics(log_line, total_file_size, status_code_counts):
    '''Updates the metrics from a given HTTP request log.

    Args:
        log_line (str): A line from the HTTP request log.
        total_file_size (int): Total file size accumulated.
        status_code_counts (dict): Dictionary containing counts
            of status codes.

    Returns:
        int: The new total file size.
    '''
    info = extract_request_info(log_line)
    if info:
        status_code = info['status_code']
        status_code_counts[status_code] = status_code_counts.get(status_code, 0)
        status_code_counts[status_code] += 1
        total_file_size += info['file_size']
    return total_file_size


def run():
    '''Starts the log parser and computes statistics.'''
    line_num = 0
    total_file_size = 0
    status_code_counts = {
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
            log_line = input()
            total_file_size = update_metrics(
                log_line,
                total_file_size,
                status_code_counts,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_code_counts)


if __name__ == '__main__':
    run()
