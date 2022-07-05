#!/usr/bin/python3
"""
Module 2-is_same_class.py
same instance
and methods
"""


def inherits_from(obj, a_class):
    """ is the objec is exactly an instance of the specified class """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
