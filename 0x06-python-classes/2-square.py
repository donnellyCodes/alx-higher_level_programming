#!/usr/bin/python3
"""Defines class square
by creating class Square.
"""


class Square:
    """
    Class that defines properties a square by: (based on 1-square.py).
    Attribute:
        size: size of the square.
    """
    def __init__(self, size=0):
        """Using size as an object, it must be an integer else a TypeError
        occurs with additional message.
        Attribute:
            __size: is private
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
