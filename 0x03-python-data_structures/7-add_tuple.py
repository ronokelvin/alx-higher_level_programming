#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples.

    Args:
        tuple_a (tuple): First tuple to be added.
        tuple_b (tuple): Second tuple to be added.

    Returns:
        tuple: A tuple containing the sum of corresponding elements
                 from input tuples.
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
