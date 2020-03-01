# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pyQt5
   Description :
   Author :       杨敏和
   date：         2020/1/28 00:36
-------------------------------------------------
   Change Activity:
                   2020/1/28:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings
from PyQt5.Qt import *

#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers=logging.getLogger('log')



if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    # QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类。
    w = QWidget()
    # resize()方法调整窗口的大小。这离是250px宽150px高
    w.resize(400, 400)
    # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
    w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle('双佳APK包')
    # 显示在屏幕上
    w.show()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())