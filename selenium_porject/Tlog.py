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
import logging
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 创建日志的路径
LOG_PATH = os.path.join(BASE_DIR, 'logs')
# 如果地址不存在，则自动创建log文件夹
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

# encoding:utf-8
import sys
import logging
import time
def writeLog(message):
  logger=logging.getLogger()
  filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))
  handler=logging.FileHandler("logs"+filename+"error")
  logger.addHandler(handler)
  logger.setLevel(logging.NOTSET)
  logger.info(message)
if __name__ == '__main__':
  Tlog =writeLog()
