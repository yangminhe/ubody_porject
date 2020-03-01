# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     practice
   Description :
   Author :       杨敏和
   date：         2020/1/28 15:53
-------------------------------------------------
   Change Activity:
                   2020/1/28:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings
#引入xlrd包
import xlrd
#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')

#将Excel文件变成变量
filename=r'/Users/Macx/pycharm_porject/ubody_porject/xlrd/xlrd.xlsx'
#使用函数open_workbook打开Excle文件
workBook=xlrd.open_workbook(filename)
#使用函数sheet_names展示Excle工作表
print(workBook.sheet_names())
#直接获取工作表
table=workBook.sheet_by_name('测试')

print("总行数：" + str(table.nrows))
print("总列数：" + str(table.ncols))
print("整行值：" + str(table.row_values(0)))
print("整列值：" + str(table.col_values(0)))
#这里用cell函数展示Excle数据，获取单元格数据
cel_B3 = table.cell(0,0).value
print("第1行第1列的值：" + str(cel_B3))

'''
使用for循环遍历Excle表的数据
1、这里使用了几个函数
range函数创建一个整数列表
col_values获取Excle的列值
enumerate函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
'''
row=table.ncols

for i in range(row):
    rowdate=table.col_values(i)
    for a,b in enumerate(rowdate):
        print(b)

print(range(row))