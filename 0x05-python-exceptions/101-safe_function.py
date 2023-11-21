#!/usr/bin/python3
# 101-safe_function.py

import sys

def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to be executed.
        args: Arguments to pass to fct.

    Returns:
        Returns the result of the function execution, or None if an error occurs.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
