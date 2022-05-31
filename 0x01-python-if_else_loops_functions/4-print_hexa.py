#!/usr/bin/python3
for i in range(0, 99):
    j = int(i/16)
    k = i % 16
    for l in range(6):

    print("{} = 0x{}".format(i, j*10+k))
