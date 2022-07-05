#!/usr/bin/python3
"""Define object-to-text method using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """return json representation"""
    with open(filename, "w") as myFile:
        return json.dump(my_obj, myFile)
