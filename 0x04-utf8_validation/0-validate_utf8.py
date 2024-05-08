#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """ Determine if given dataset is valid UTF-8 encoding."""
    # Number of bytes
    nb_b = 0

    # Iterate through each int in data list
    for byte in data:
        if nb_b == 0:
            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                nb_b = 1
            elif byte >> 4 == 0b1110:
                nb_b = 2
            elif byte >> 3 == 0b11110:
                nb_b = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            nb_b -= 1

    return nb_b == 0
