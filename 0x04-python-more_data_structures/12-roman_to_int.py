#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    sum = 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'I':
            if i != len(roman_string) - 1:
                if roman_string[i+1] == 'I':
                    sum += 1
                else:
                    sum -= 1
            else:
                sum += 1
        elif roman_string[i] == 'V':
            sum += 5
        elif roman_string[i] == 'X':
            sum += 10
        elif roman_string[i] == 'L':
            sum += 50
        elif roman_string[i] == 'C':
            sum += 100
        elif roman_string[i] == 'D':
            sum += 500
        elif roman_string[i] == 'M':
            sum += 1000
    return sum
