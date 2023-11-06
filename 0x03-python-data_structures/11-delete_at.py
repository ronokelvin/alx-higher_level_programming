#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """
    Delete an item at a specific position in the given list.

    Args:
        my_list (list): The list from which the item will be deleted.
        idx (int): The index of the item to be deleted.

    Returns:
        list: The updated list after deleting the item,
              or the original list if the index is out of bounds.
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
