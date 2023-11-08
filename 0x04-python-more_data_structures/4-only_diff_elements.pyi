#!/usr/bin/python3
# 4-only_diff_elements.py


def only_diff_elements(set_1, set_2):
    """
    Return a set of elements that are present in only one of the input sets.

    :param set_1: The first set.
    :param set_2: The second set.
    :return: A set containing elements unique to one of the input sets.
    """
    return (set_1 ^ set_2)
