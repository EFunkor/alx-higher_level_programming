#!/usr/bin/python3
"""
A script to compute metrics from log data read from stdin.
Input format: <IP Address> -
[<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Prints metrics every 10 lines or after a keyboard interruption (CTRL + C).
"""

import sys


def print_metrics(total_size, status_codes):
    """Prints the computed metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404:
                    0, 405: 0, 500: 0}
    line_count = 0

    for line in sys.stdin:
        line_count += 1
        try:
            data = line.split()
            total_size += int(data[-1])
            status = int(data[-2])
            if status in status_codes:
                status_codes[status] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

        except Exception as e:
            pass

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
