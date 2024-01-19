#!/usr/bin/python3

"""defining rectangle class"""


class Rectangle:
    """defining and initializing objects"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """defining width"""
    def width(self):
        return self.__width

    """setting the width"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """defining height"""
    def height(self):
        return self.__height

    """setting the height"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """defining the area"""
    def area(self):
        return self.width * self.height

    """defining the perimeter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    """defining representation of string"""
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    """detecting if the instance are destroyed"""
    def __del__(self):
        print("Bye rectangle...")
