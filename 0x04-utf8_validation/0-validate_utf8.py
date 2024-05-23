#!/usr/bin/python3
"""
This module contains a function to validate if a given data set represents
a valid UTF-8 encoding. The data set is provided as a list of integers,
where each integer represents a byte (0 <= x <= 255). The function
validUTF8(data) returns True if the data is a valid UTF-8 encoding,
else returns False.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (list): A list of integers where each integer represents
    a byte (0 <= x <= 255).

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 | mask2)) == mask1:
                return False
            elif (byte & (mask1 | mask2 | (mask2 >> 1))) == (mask1 | mask2):
                num_bytes = 1
            elif (byte & (mask1 | mask2 | (mask2 >> 1) | (mask2 >> 2))) == (
                mask1 | mask2 | (mask2 >> 1)
            ):
                num_bytes = 2
            elif (byte & (
                mask1 | mask2 | (mask2 >> 1) | (mask2 >> 2) | (mask2 >> 3)
            )) == (mask1 | mask2 | (mask2 >> 1) | (mask2 >> 2)):
                num_bytes = 3
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
