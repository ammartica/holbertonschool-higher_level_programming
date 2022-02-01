#!/usr/bin/python3
"""Defines a class named Rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the data"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance method returns rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """public instance method returns rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """returns printable string that represents rectangle"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            for j in range(self.width):
                string += "#"
            if i != self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """returns string representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """prints message when instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
