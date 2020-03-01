# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_Myclass2
   Description :
   Author :       杨敏和
   date：         2020/2/13 01:05
-------------------------------------------------
   Change Activity:
                   2020/2/13:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings
import unittest
from ddt_cas.Myclass_test import Myclass_test

#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')

class Test_Myclass2(unittest.TestCase):

    def setUp(self):
        self.myclass = Myclass_test(1,12)

    def test_sum(self):
        print("sum_2")
        sum = self.myclass.sum()
        self.assertEqual(13,sum)

    def test_sub(self):
        print("sub_2")
        sub = self.myclass.sub()
        self.assertEqual(-11,sub)
