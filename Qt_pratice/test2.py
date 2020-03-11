# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test2
   Description :
   Author :       杨敏和
   date：         2020/3/10 14:28
-------------------------------------------------
   Change Activity:
                   2020/3/10:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings

#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')


class father():
    def __init__(self):
        self._name = "aaa"

    def fun1(self):
        method = eval('self.' + 'ss' + '_db')
        print(method)

    def fun2(self):
        tt = self.ss_db
        print(tt)


class son(father):
    def __init__(self):
        father.__init__(self)
        self.ss_db = "daas"

    def getname(self):
        print(self._name)
        return self._name


if __name__ == "__main__":
    son = son()
    son.fun1()
    son.fun2()
    son.getname()
