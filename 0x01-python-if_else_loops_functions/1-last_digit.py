#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number:d} is {number%10:d} and")
if number%10 > 5:
    print("is greater than 5")
elif number%10 == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
