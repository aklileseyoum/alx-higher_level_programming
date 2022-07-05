#!/usr/bin/python3
"""
Module 9-rectangle
inherits from rectangle
Class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle"""

    def __init__(self, size):
        """validate and initialize size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate area"""
        return self.__size**2
