#!usr/bin/python3
"""Define rectangle class model"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherts from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method to initialize the variables"""
        super(). __init__(id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    #getter method for width
    def get_width(self):
        return self.width

    #setter method for width
    def set_width(self, width):
        self.width = width

    #getter method for height
    def get_height(self):
        return self.height

    #setter method for height
    def set_height(self, h):
        self.height = h

    #getter method for x
    def get_x(self):
        return self.x

    #setter method for x
    def set_x(self, x):
        self.x = x

    #getter method for y
    def get_y(self):
        return self.y

    #setter method for y
    def set_y(self, y):
        self.y = y
