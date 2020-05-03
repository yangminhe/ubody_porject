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
class dboperation():
    # 打开数据库连接
    db =pymysql.connect(host='rds0cxlu1x8n4a289397132.mysql.rds.aliyuncs.com',
        user='ubodydbuser',
        passwd='k3n9P_8Knaf',
        db='ubody_organization',
        charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = """insert into app_version(av_url,av_name,av_version,av_desc,av_status,av_addtime,av_edittime) values(
            'http://api.ubody.net/apk/SK-GS2-OTC-XB.apk','SK-GS2-OTC-XB',18,'1、修改产品展示跟动销话术的内容',1,
            '2020-04-29 22:42:37','2020-04-29 22:42:41');"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


if __name__=='__mian__':
    rundb=dboperation
    rundb.close()