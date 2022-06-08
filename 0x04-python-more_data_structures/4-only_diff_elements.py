#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set_1.difference(set_2)
    new2 = set_2.difference(set_1)
    for i in new2:
        new.add(i)
    return new
