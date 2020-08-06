#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/6

import xlrd

# 打开数据所在的路径表名
book = xlrd.open_workbook('dd.xlsx')
# 这个是表里的sheet名称（注意大小写）
sheet = book.sheet_by_name('Sheet1')

print(sheet.row(1))
print(sheet.cell(1, 1))
print(sheet.cell_type(1, 3))
d = xlrd.xldate.xldate_as_datetime(sheet.cell(1, 4).value, 0)
print(d)
print(type(d))
