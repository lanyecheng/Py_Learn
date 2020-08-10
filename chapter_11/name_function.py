#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/10

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
