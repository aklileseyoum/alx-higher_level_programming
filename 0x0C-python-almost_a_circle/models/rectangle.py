#!usr/bin/python3
"""Define rectangle class model"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherts from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method to initialize the variables"""
        super(). __init__(id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    #getter method for width
    def get_width(self):
        return self.__width

    #setter method for width
    def set_width(self, width):
        self.__width = width

    #getter method for height
    def get_height(self):
        return self.__height

    #setter method for height
    def set_height(self, h):
        self.__height = h

    #getter method for x
    def get_x(self):
        return self.__x

    #setter method for x
    def set_x(self, x):
        self.__x = x

    #getter method for y
    def get_y(self):
        return self.__y

    #setter method for y
    def set_y(self, y):
        self.__y = y
