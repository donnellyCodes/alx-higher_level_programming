#!/usr/bin/python3
"""
Class rectangle
"""


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
            return (self.__width * self.__height)

        def perimeter(self):
            if (self.__width == 0 or self.__height == 0):
                return 0
            else:
                return (2 * (self.__width + self.__height))

        def __str__(self):
            if self.__width == 0 or self.__height == 0:
                return ("")

            rectangle = []
            for i in range(self.__height):
                [rectangle.append(str(self.print_symbol))
                 for j in range(self.__width)]
                if i != self.__height - 1:
                    rectangle.append("\n")
            return ("".join(rectangle))

        def __repr__(self):
            rectangle = "Rectangle(" + str(self.__width)
            rectangle = rectangle + ", " + str(self.__height) + ")"
            return (rectangle)

        def __del__(self):
            Rectangle.number_of_instances -= 1
            print("Bye rectangle...")
