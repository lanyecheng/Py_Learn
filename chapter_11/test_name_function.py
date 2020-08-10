#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/10

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试 name_function.py """

    def test_first_last_name(self):
        """测试 get_formatted_name 函数是否正确输出 """
        formatted_name = get_formatted_name('lan', 'cheng')
        self.assertEqual(formatted_name, 'Lan Cheng')

    def test_first_middle_last_name(self):
        """测试 get_formatted_name 函数是否正确输出 """
        formatted_name = get_formatted_name('lan', 'cheng', 'ye')
        self.assertEqual(formatted_name, 'Lan Ye Cheng')


if __name__ == "__manin__":
    unittest.main()
