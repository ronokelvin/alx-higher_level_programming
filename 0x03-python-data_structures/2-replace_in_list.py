#!/usr/bin/python3
# 2-replace_in_list.py

def replace_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position.

    Args:
        my_list (list): The list in which replacement will occur.
        idx (int): The index of the element to be replaced.
        element: The new element to replace with.

    Returns:
        list: The modified list with the replacement.

    Note:
        This function replaces the element at the given index
          with the new element.
        If the index is out of bounds, the original list remains unchanged.
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
