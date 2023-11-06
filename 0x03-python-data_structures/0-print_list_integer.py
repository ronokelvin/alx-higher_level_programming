#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """
    Print all the integers in a given list.

    Args:
        my_list (list): The list containing integers to be printed.
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
