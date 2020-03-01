# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     practice
   Description :
   Author :       杨敏和
   date：         2020/1/19 18:14
-------------------------------------------------
   Change Activity:
                   2020/1/19:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings

#引用日志配置
logging.config.dictConfig(settings.LOGGING)
loggers=logging.getLogger('log')

# !/usr/bin/python3

# num = 1
#
#
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     # print(num)
#     num = 123
#     print(num)
#
#
# fun1()
# # print(num)
#
# def printme( str ):
#    "打印传入的字符串到标准显示设备上"
#    print (str)
#    return '不知道'
#
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")

#
# x = 1
# y = 2
# def add (x, y):
#     z = x + y
#     return(z)
# print(add(x,y))
#
#
# x = 1
# y = 2
# def add (x, y):
#     z = x + y
#     print(z)
# print(add(x,y))


def func():
    try:
        # print(98)
        return 'ok'  # 函数得到了一个返回值
    finally:  # finally语句块中的语句依然会执行
        print(98)
print (func())