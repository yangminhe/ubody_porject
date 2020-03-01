# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Myclass_main
   Description :
   Author :       杨敏和
   date：         2020/2/13 01:07
-------------------------------------------------
   Change Activity:
                   2020/2/13:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings
import unittest
from BeautifulReport import BeautifulReport
import time

startime=time.strftime("%Y-%m-%d",time.localtime())
#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')
#实例化测试套件对象
s = unittest.TestSuite()
#实例化TestLoader的对象
loader = unittest.TestLoader()
#使用discover()去找一个目录下的所有测试用例的文件,并将返回数据添加到测试套件中。
s.addTests(loader.discover(os.getcwd()))
runner =BeautifulReport(s)
runner.report(filename=startime+'测试', description='测试deafult报告', report_dir='report', theme='theme_default')
