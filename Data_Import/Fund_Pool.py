#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/6

import xlrd
import pymysql

# 打开数据所在的路径表名
book = xlrd.open_workbook('C:\\Users\\lanyecheng\\Desktop\\中欧投顾基金备投池导入.xlsx')
# 这个是表里的sheet名称（注意大小写）
sheet = book.sheet_by_name('Sheet1')

# 建立一个 MySQL连接
conn = pymysql.connect(
    host='xxx',
    user='xxx',
    passwd='xxx',
    db='xxx',
    port=10096,
    charset='utf8'
)

# 获得 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
# 创建插入sql语句
query = "INSERT INTO tb_tg_strategy_fund_pool (" \
        "c_investconsultid, c_investconsultname, c_strategyid, c_strategyname, c_displayid, c_fundcode, c_fundname, " \
        "c_isenable, c_islinked, c_removedtime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for r in range(1, sheet.nrows):
    c_investconsultid = sheet.cell(r, 0).value
    c_investconsultname = sheet.cell(r, 1).value
    c_strategyid = sheet.cell(r, 2).value
    c_strategyname = sheet.cell(r, 3).value
    c_displayid = sheet.cell(r, 4).value
    c_fundcode = sheet.cell(r, 5).value
    c_fundname = sheet.cell(r, 6).value
    c_isenable = sheet.cell(r, 7).value
    c_islinked = sheet.cell(r, 10).value
    c_removedtime = None
    values = (c_investconsultid, c_investconsultname, c_strategyid, c_strategyname, c_displayid, c_fundcode, c_fundname,
              c_isenable, c_islinked, c_removedtime)
    # 执行sql语句
    cursor.execute(query, values)

cursor.close()
conn.commit()
conn.close()

columns = str(sheet.ncols)
# 显示导入多少行
rows = str(sheet.nrows)
print('导入' + columns + '列' + rows + '行数据到MySQL数据库!')
