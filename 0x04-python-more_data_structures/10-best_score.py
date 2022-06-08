#!/usr/bin/python3
def best_score(a_dictionary):
    values = a_dictionary.values()
    high = 0
    for i in values:
        if i > high:
            high = i
    for k, v in a_dictionary.items():
        if high == v:
            return k
