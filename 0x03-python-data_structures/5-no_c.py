#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """
    Remove all occurrences of the characters 'c' and 'C' from a string.

    Args:
        my_string (str):
                 The input string from which characters are to be removed.
     Returns:
        str: A new string with 'c' and 'C' removed.
    """
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return "".join(copy)
