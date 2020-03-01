# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ${NAME}
   Description :
   Author :       杨敏和
   date：         ${DATE} ${TIME}
-------------------------------------------------
   Change Activity:
                   ${DATE}:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings
#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers=logging.getLogger('log')
