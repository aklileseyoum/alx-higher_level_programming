#!/usr/bin/python3
"""
Module 2-append_write
append a text to a file
method
"""


def append_write(filename="", text=""):
    """append a text to a file"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
