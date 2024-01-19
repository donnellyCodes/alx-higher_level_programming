#!/usr/bin/python3
"""Defining a class rectangle"""
class Rectangle:
    """initializing the objects width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """to retrieve the private instance"""
    def width(self):
        return self.__width

    """to set the private instance width"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """to retrieve private instance height"""
    def height(self):
        return self.__height

    """to set the height instance"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
