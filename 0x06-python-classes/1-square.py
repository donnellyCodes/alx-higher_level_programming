#!/usr/bin/python3
"""Defines class square"""
class Square:
    """
    Class that defines properties a square by: (based on 0-square.py).
    Attribute:
        size: size of the square.
    """
    def __init__(self, size):
        """Creating a new object of a square.
        Attribute:
            __size: is private
        """
        self.__size = size
