# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Myclass_test
   Description :
   Author :       杨敏和
   date：         2020/2/10 01:23
-------------------------------------------------
   Change Activity:
                   2020/2/10:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings

#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')

class Myclass_test:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        sum = self.a + self.b
        return sum

    def sub(self):
        sub = self.a - self.b
        return sub
