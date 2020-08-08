#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/8

import json

filename = 'username.json'

with open(filename) as j_boj:
    username = json.load(j_boj)
    print("Welcome back, " + username + "!")
