#!/usr/bin/python3
"""Defines class square
by creating class Square.
"""


class Square:
    """
    Class that defines properties a square by: (based on 3-square.py).
    Attribute:
        size: size of the square is 0.
    """
    def __init__(self, size=0):
        """Creating a new object of a square.
        Attribute:
            __size: is private
        """
        self.__size = size

    @property
    def size(self):
        """def size(self) is used as property
        to carry out getter function.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """def size(size, value) is used to perform
        getter function to get size that is declared private
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the area of the square
        """
        return self.__size ** 2
