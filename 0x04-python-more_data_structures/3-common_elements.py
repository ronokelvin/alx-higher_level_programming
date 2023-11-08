#!/usr/bin/python3
# 3-common_elements.py

def common_elements(set_1, set_2):
    """
    Return a set containing the common elements between two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A new set containing the common elements.
    """
    return set_1 & set_2
