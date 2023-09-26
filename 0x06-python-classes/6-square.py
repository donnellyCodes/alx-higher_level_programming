#!/usr/bin/python3
"""Defines class square
by creating class Square.
"""


class Square:
    """
    Class that defines properties a square by: (based on 5-square.py).
    Attribute:
        size: size of the square which is 0.
        position: positon of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creating a new object
        Attribute:
            size: is private
            position: is private
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        used as a getter to return size of a square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """performs function of a setter to retrieve size of a
        square if size is not an integer, an error is returned and a statement.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        used as a getter to return position in a tupel.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """performs setter function to retrieve position of a square
        in tuple.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 postive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """ a public instance method used to print is stdout
        the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range (self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
