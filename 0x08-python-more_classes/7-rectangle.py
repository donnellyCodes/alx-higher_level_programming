#!/usr/bin/python3

class Rectangle:
    """"defines a rectangle by it's width and height"""


    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes a new instance of the rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

        @property
        def width(self):
            """Gets width of the rectangle"""
            return self.width

        @width.setter
        def width(self, value):
            """sets width of the rectangle"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """Gets the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets height of the rectangle"""
            if not istnstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        def area(self):
            return self.width * self.height
        
        def perimeter(self):
            if self.width == 0 or self.height == 0:
                return 0
            else:
                return 2 * (self.width + self.height)

        def __str__(self):
            if self.width == 0 or self.height == 0:
                return ""
            else:
                return "/n".join([Rectangle.print_symbol * self.width] * self.height)

        def __repr__(self):
            return f"Rectangle({self.width}, {self.height})"
        def __del__(self):
            Rectangle.number_of_instances -= 1
            print("Bye rectangle" + "..." * 3)
