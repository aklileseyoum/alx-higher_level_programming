#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    found = 0
    for k, v in a_dictionary.items():
        if k == key:
            found = 1
            a_dictionary.update({key: value})
    if found == 0:
        a_dictionary[key] = value
    return a_dictionary
