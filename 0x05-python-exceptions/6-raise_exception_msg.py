#!/usr/bin/python3
# 6-raise_exception_msg.py

def raise_exception_msg(message=""):
    """
    Raises a NameError exception with the provided message.

    Args:
        message (str): The message to include in the exception.

    Raises:
        NameError: Always raises a NameError with the given message.
    """
    raise NameError(message)
