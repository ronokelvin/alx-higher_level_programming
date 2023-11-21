#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Safely prints a specified number of elements from a list.

    This function prints the first 'x' elements of the given list without
    causing an IndexError if the index is out of range.

    Args:
        my_list (list): The list from which elements will be printed.
        x (int): The number of elements to print.

    Returns:
        The number of elements successfully printed.
    """
    elements_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements_printed += 1
        except IndexError:
            break
    print("")
    return (elements_printed)
