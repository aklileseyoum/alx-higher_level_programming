#!/usr/bin/python3
"""
Module 6-rectangle
Contains class Rectangle with private attribute width and height,
public area and perimeter methods, allows printing #'s, deletes,
and has public attribute to keep track of number of instances
"""


class Rectangle():
    """
    Defines class rectangle with private attribute width and height
    Args:
        width (int): width
        height (int): height
    Attributes:
        number_of_instances (int): number of instances created and not deleted
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ Deletes instance of class """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:

