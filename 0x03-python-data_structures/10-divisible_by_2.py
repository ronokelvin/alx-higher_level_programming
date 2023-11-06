#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Identify elements in the list that are divisible by 2.

    Args:
        my_list (list): List of integers to be checked.

    Returns:
        list: A list of boolean values indicating whether each element
                is divisible by 2.
    """
    divisible_flags = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            divisible_flags.append(True)
        else:
            divisible_flags.append(False)

    return divisible_flags
