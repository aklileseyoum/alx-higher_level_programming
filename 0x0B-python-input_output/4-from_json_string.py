#!/usr/bin/python3
"""Define string-to-object function"""
import json


def from_json_string(my_str):
    """change string to object"""
    return json.loads(my_str)
