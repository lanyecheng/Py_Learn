#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/8

import json


def get_stored_username():
    """如果用户存储了用户名，就获取它"""
    file_name = 'username.json'
    try:
        with open(file_name) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """问候用户，并指出其姓名"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("what is your name? ")
        file_name = 'username.json'
        with open(file_name, 'w') as f_obj:
            json.dump(username, f_obj)
            print("we'll remember you when you come back, " + username + "!")


greet_user()
