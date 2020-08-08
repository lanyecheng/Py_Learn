#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/8

filename = 'programming.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    print(words)
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
