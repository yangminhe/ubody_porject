# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     settings.py
   Description :
   Author :       杨敏和
   date：         2020/1/6 14:18
-------------------------------------------------
   Change Activity:
                   2020/1/6:
-------------------------------------------------
"""
#导入配置的文件包
from blog.object import settings
#使用logging包的config方法
import logging.config
#引用logging.config的dictConfig方法，注意这里要带文件名settings，否则无法使用LOGGING方法
logging.config.dictConfig(settings.LOGGING)
loggers=logging.getLogger('log')

#这里不用logging的记录器，直接使用logging的方法去调用日志leve
loggers.error('2213')
loggers.info('2344444')
