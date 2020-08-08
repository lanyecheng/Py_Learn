#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/8

import json

numbers = [2, 3, 4, 5, 6, 7]
filename = 'number.json'
with open(filename, 'w') as f_boj:
    json.dump(numbers, f_boj)
