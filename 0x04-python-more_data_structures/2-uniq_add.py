#!/usr/bin/python3
# 2-uniq_add.py


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list, summing each integer only once.

    Args:
        my_list (list): A list of integers.

    Returns:
        int: The sum of unique integers in the list.
    """
    result = 0
    for x in set(my_list):
        result += x
    return result
