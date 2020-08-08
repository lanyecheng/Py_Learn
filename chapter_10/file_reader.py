#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/3

# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# with open('pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)

new_file = 'programming.txt'
with open(new_file, 'a') as new_file_object:
    new_file_object.write('I love programming.\n')
    new_file_object.write('I love creating new games.\n')
