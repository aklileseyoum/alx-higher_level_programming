#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k, v in a_dictionary.items():
        if k == key:
            a_dictionary.pop(k)
            break
    return a_dictionary
