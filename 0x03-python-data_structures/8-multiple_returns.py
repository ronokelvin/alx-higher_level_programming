#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """
    Returns a tuple containing the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing two elements:
                     the length of the string and its first character.
               If the input string is empty, (0, None) is returned.
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
