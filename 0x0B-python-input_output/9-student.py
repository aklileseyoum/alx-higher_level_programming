#!/usr/bin/python3
"""
Module 9-student
create dictionary representation for class instance
class
"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
