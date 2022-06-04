#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == 'c':
            for j in range(i, len(my_string)):
                my_string[j] = my_string[j + 1]
    return my_string

