#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    """
    Safely divides a by b and returns the result.

    Args:
        a (int): Numerator.
        b (int): Denominator.

    Returns:
        float: The result of division if successful, None otherwise.
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
