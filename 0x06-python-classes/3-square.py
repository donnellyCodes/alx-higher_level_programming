#!/usr/bin/python3
"""Defines class square
by creating class Square.
"""


class Square:
    """
    Class that defines properties a square by: (based on 2-square.py).
    Attribute:
        size: size of the square is 0.
    """
    def __init__(self, size=0):
        """
        Creating a new object size with optional size which must be
        an integer else an error occurs with a message.
        Attribute:
            __size: is private.
        Method:
            def area(self): returns current square area.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
