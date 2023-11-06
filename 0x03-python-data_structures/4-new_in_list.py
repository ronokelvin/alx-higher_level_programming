#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """
    Replace an element in a copied list at a specified position.

    Args:
        my_list (list): The original list.
        idx (int): Index of the element to be replaced.
        element: The new element to replace the old one.

    Returns:
        list: A new list with the specified element replaced,
               or the original list if the index is out of bounds.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    copy = [x for x in my_list]
    copy[idx] = element
    return copy
