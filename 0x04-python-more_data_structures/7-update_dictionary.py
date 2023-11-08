#!/usr/bin/python3
# 7-update_dictionary.py

def update_dictionary(a_dictionary, key, value):
    """
    Replace or add key/value pairs in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key: The key to replace or add.
        value: The value to associate with the key.

    Returns:
        dict: The updated dictionary with the key/value pair.
    """
    a_dictionary[key] = value
    return (a_dictionary)
