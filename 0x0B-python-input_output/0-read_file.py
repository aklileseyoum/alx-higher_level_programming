#!/usr/bin/python3
"""
Module 0-read_file
reads file
Method
"""

def read_file(filename=""):
    """read the given file"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end=" ")
