#!/usr/bin/python3
# 1-search_replace.py


def search_replace(my_list, search, replace):
    """
    Replace all instances of a specified element with another in a new list.

    :param my_list: The original list.
    :param search: The element to search for in the list.
    :param replace: The element to replace the 'search' element with.
    :return: A new list with the specified replacements.
    """
# Create a copy of the original list to avoid modifying it directly.
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
