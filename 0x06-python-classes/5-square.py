#!/usr/bin/python3
"""Defines class square
by creating class Square.
"""


class Square:
    """
    Class that defines properties a square by: (based on 0-square.py).
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
        """used as a property to represent a
        getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """is a property setter the value must be an integer
        otherwise an error is obtained with additional
        message.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns the area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """public instance method that prints in stdout
        the square with # character
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
