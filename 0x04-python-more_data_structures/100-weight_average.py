#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    product = 1
    summ = 0
    per = 0
    for k, v in my_list.items():
        product = k * v
        summ += product
        per += v
    return summ / per
