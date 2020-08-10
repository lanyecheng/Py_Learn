#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/10

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """ 针对 AnonymousSurvey 类的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案，提供测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """ 测试单个答案会被妥善地存储"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        """ 测试单个答案会被妥善地存储"""
        for i in self.responses:
            self.my_survey.store_responses(i)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__manin__":
    unittest.main()
