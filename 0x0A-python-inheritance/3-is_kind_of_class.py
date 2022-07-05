#!/usr/bin/python3
"""
    Module 3-is_kind_of_class
    kind same instance
    and methods
"""
def is_kind_of_class(obj, a_class):
     """ if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class """
    return isinstance(obj, a_class)
