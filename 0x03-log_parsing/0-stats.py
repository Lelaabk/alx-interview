#!/usr/bin/python3

import sys


def print_line(dict_l, total_sz):
    """
    Parse a log line and extract 
    IP address, status code, and file size.
    """

    print("File size: {}".format(total_sz))
    for key, val in sorted(dict_l.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_sz = 0
code = 0
c = 0
dict_l = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_l = line.split()
        parsed_l = parsed_l[::-1]

        if len(parsed_l):
            c += 1

            if c <= 10:
                total_sz += int(parsed_l[0])
                code = parsed_l[1]

                if (code in dict_l.keys()):
                    dict_l[code] += 1

            if (c == 10):
                print_line(dict_l, total_sz)
                c = 0

finally:
    print_line(dict_l, total_sz)
