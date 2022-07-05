#!/usr/bin/python3
"""
Module 1-write_file
to write to a file
Method
"""


def write_file(filename="", text=""):
    """writes to a file and returns number of characters"""
    with open(filename, "w", encoding="utf-8") as myFile:
        """opens a file in writing mode"""
        return myFile.write(text)
