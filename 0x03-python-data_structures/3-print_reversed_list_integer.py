#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """
    Print all the integers in reverse order from a given list.

    :param my_list: A list of integers.
    :type my_list: list
    """
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
