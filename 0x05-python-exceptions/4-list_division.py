#!/usr/bin/python3
# 4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    """Element-wise division of two lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): Number of elements to divide.

    Returns:
        A new list of length list_length containing division results.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Type error")
            div = 0
        except ZeroDivisionError:
            print("Division by zero")
            div = 0
        except IndexError:
            print("Index out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
