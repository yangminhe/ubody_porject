# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ftp_for
   Description :
   Author :       杨敏和
   date：         2020/2/22 10:49
-------------------------------------------------
   Change Activity:
                   2020/2/22:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings
import sys
from PyQt5.Qt import *
from server_linux.ftp_for import Putserver

# 引用日志配置
logging.config.dictConfig(settings.LOGGING)
# 引用日志记录器
loggers = logging.getLogger('log')


# path = os.path.dirname(os.path.realpath(__file__))
# print(path)


class Winos(QWidget):

    def __init__(self):
        super().__init__()  # 调用父类

        self.initUI()  # 绘制界面方法initUI,不固定，可以给其它值

    def initUI(self):
        # 打印浏览地址
        self.open_path_text = QLineEdit(self)
        self.open_path_text.setGeometry(QRect(30, 22, 250, 23))
        self.open_path_text.setPlaceholderText("打开地址")

        # 创建按钮选取文件
        self.btn = QPushButton('浏览', self)
        self.btn.setGeometry(QRect(280, 22, 75, 23))
        self.btn.clicked.connect(self.openfile)

        self.btn1 = QPushButton('保存', self)
        self.btn1.setGeometry(QRect(280, 50, 75, 23))
        self.btn1.clicked.connect(self.savefile)

        # 这里是创建窗口
        self.setGeometry(400, 400, 400, 300)
        self.setWindowTitle('双佳APK')
        self.setWindowIcon(QIcon('cloud.ico'))
        self.center()
        self.show()

    # center是QT显示在屏幕中间窗口属性
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openfile(self):
        fileName1 = QFileDialog.getOpenFileName(self, "选取文件")
        print(fileName1)
        path = fileName1[0]
        #文件地址存储
        self.open_path_text.setText(path)
        path_load = open("path_load", "w" ,encoding="utf-8")
        path_load.write(path)
        #文件名字存储
        f = QFileInfo(path)
        file_name = f.fileName()
        print(file_name)
        Na = open("file_os", "w", encoding="utf-8")
        Na.write(file_name)
        # path_load.close()

    def savefile(self):
        "调用paramiko连接服务器并保存"
        save = Putserver()
        save.putconnet()



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
    ex = Winos()
    sys.exit(app.exec_())
