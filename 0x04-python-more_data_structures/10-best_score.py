#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_directory:
        return "None"
    values = a_dictionary.values()
    high = 0
    for i in values:
        if i > high:
            high = i
    for k, v in a_dictionary.items():
        if high == v:
            return k
