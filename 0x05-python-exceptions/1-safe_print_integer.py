#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """Prints an integer using the format specifier "{:d}".

    Args:
        value (int): The integer value to be printed.

    Returns:
        Returns True if the integer was successfully printed.
        Returns False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
