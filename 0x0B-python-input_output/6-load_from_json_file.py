#!/usr/bin/python3
"""Define function that create object from json file"""
import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename, "r", encoding="utf-8") as myFile:
        obj = json.load(myFile)
    return obj
