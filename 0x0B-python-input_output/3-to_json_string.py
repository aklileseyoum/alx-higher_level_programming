#!/usr/bin/python
"""Defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """change object to json"""
    return json.dumps(my_obj)
