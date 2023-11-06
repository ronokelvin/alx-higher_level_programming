#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """
    Finds the largest integer in a list.

    Args:
        my_list (list): The list of integers to be processed.

    Returns:
        int or None: The largest integer in the list,
                       or None if the list is empty.
    """
    if len(my_list) == 0:
        return None

    largest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    return largest
