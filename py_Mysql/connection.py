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
import time

#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')

# 打开数据库连接
db =pymysql.connect(host='120.24.239.10',
    port=3306,
    user='root',
    passwd='123456',
    db='public_health',
    charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """insert into role_user(user_id,role_id) values(1523,5)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()