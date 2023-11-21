#!/usr/bin/python3
# 103-magic_calculation.py
"""Define a MagicClass that corresponds to a provided bytecode by Holberton."""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass instance.

        Args:
            radius (float or int): The radius of the MagicClass circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the MagicClass circle."""
        return 2 * math.pi * self.__radius
