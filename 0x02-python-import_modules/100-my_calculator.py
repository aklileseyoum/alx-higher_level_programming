#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    n = argv[2]
    if n == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
        print(0)
        exit(0)
    elif n == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
        print(0)
        exit(0)
    elif n == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
        print(0)
        exit(0)
    elif n == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        print(0)
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        print(1)
        exit(1)
