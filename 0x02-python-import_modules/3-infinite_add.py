#!/usr/bin/python3
from sys import argv
s =  0
for i in range(1, len(argv)):
    s = s + int(argv[i])
print(s)
