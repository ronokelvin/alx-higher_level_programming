#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys

def safe_print_integer_err(value):
    """Safely prints an integer using "{:d}".format().

    This function attempts to print an integer value using
    the "{:d}".format() method. If the value is not an integer
    or if a ValueError occurs, an error message is printed to
    the standard error stream.

    Args:
        value (int): The integer value to print.

    Returns:
        bool: True if the value was printed successfully,
              False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        error_message = "Exception: {}".format(sys.exc_info()[1])
        print(error_message, file=sys.stderr)
        return False
