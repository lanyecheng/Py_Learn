#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/8/6

import xlrd
import pymysql

# 打开数据所在的路径表名
book = xlrd.open_workbook('C:\\Users\\lanye\\Desktop\\慧投一号产品止盈情况汇总-导入.xlsx')
# 这个是表里的sheet名称（注意大小写）
sheet = book.sheet_by_name('Sheet1')

# 建立一个 MySQL连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='mao1993oo',
    db='emictdb',
    port=3306,
    charset='utf8'
)

# 获得 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
# 创建插入sql语句

query = "INSERT INTO tb_tg_strategy_yield_his (" \
        "invest_consult_id, strategy_id, strategy_name, establish_day, expire_day, expire_type, run_day, end_yield," \
        "purchase_people, avg_end_yield, is_display, is_del, display_id, strategy_sub_id) " \
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


for r in range(1, sheet.nrows):
    invest_consult_id = 'JS'
    strategy_id = 34
    strategy_name = sheet.cell(r, 2).value
    establish_day = xlrd.xldate.xldate_as_datetime(sheet.cell(r, 3).value, 0)
    expire_day = xlrd.xldate.xldate_as_datetime(sheet.cell(r, 4).value, 0)
    expire = sheet.cell(r, 5).value
    if expire == '运作中':
        expire_type = '0'
    elif expire == '提前止盈':
        expire_type = '1'
    else:
        expire_type = '2'
    if sheet.cell(r, 6).value == '':
        run_day = None
    else:
        run_day = sheet.cell(r, 6).value
    if sheet.cell(r, 7).value == '':
        end_yield = None
    else:
        end_yield = str(sheet.cell(r, 7).value * 100)
    purchase_people = int(sheet.cell(r, 8).value)
    if sheet.cell(r, 9).value == '':
        avg_end_yield = None
    else:
        avg_end_yield = str(sheet.cell(r, 9).value * 100)
    if sheet.cell(r, 10).value == '':
        is_display = None
    else:
        is_display = sheet.cell(r, 10).value
    is_del = 0
    display_id = sheet.cell(r, 0).value
    strategy_sub_id = sheet.cell(r, 1).value

    values = (invest_consult_id, strategy_id, strategy_name, establish_day, expire_day, expire_type, run_day, end_yield,
              purchase_people, avg_end_yield, is_display, is_del, display_id, strategy_sub_id)
    # 执行sql语句
    cursor.execute(query, values)

cursor.close()

conn.commit()
conn.close()

columns = str(sheet.ncols)
# 显示导入多少行
rows = str(sheet.nrows)
print('导入' + columns + '列' + rows + '行数据到MySQL数据库!')
