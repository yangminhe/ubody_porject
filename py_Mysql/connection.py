# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     connection
   Description :
   Author :       杨敏和
   date：         2020/2/25 00:55
-------------------------------------------------
   Change Activity:
                   2020/2/25:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings
import pymysql

#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')
