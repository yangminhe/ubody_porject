# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     window
   Description :
   Author :       杨敏和
   date：         2020/2/25 12:22
-------------------------------------------------
   Change Activity:
                   2020/2/25:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings

#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')


import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "是否要退出?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())