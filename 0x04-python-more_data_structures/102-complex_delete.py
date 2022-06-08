#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in range(len(a_dictionary)):
        for k, v in a_dictionary.items():
            if v == value:
                a_dictionary.pop(k)
                break
    return a_dictionary
