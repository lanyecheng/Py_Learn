#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/10

class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问卷调查"""
        print(self.question)

    def store_responses(self, new_responses):
        """存储单份调查答卷"""
        self.responses.append(new_responses)

    def show_responses(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for i in self.responses:
            print('- ' + i)
