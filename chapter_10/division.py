#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/8

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me to numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
