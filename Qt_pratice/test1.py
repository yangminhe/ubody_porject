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
import paramiko
import pymysql
import time
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
        #打印文件信息
        self.open_path_text = QLineEdit()
        self.open_path_text.setEnabled(False)
        self.open_path_text.setPlaceholderText("文件地址")
        # 创建按钮选取文件
        Choosepath = QPushButton('选择文件', self)
        Choosepath.clicked.connect(self.openfile)

        # apk包信息
        PackageName = QLabel('名称')
        self.PackageNameEdit = QLineEdit()
        self.PackageNameEdit.setPlaceholderText("APK包名称")

        Vsersion = QLabel('版本号')
        self.VsersionEdit = QLineEdit()
        self.VsersionEdit.setPlaceholderText("APK包版本号")


        Information = QLabel('发版信息')
        self.InformationEdit = QTextEdit()
        self.InformationEdit.setPlaceholderText("APK包发版信息")


        Savepath = QPushButton('保存', self)
        Savepath.setGeometry(QRect(280, 270, 120, 23))
        Savepath.clicked.connect(self.savefile)


        # 用QGridLayout定义排列框架
        Debuggingbox = QGridLayout()
        Debuggingbox.setContentsMargins(1, 1, 5, 50)
        Debuggingbox.setSpacing(10)

        Debuggingbox.addWidget(self.open_path_text,1,1)
        Debuggingbox.addWidget(Choosepath,1,0)

        Debuggingbox.addWidget(PackageName, 2, 0)
        Debuggingbox.addWidget(self.PackageNameEdit, 2, 1)

        Debuggingbox.addWidget(Vsersion, 3, 0)
        Debuggingbox.addWidget(self.VsersionEdit, 3, 1)

        Debuggingbox.addWidget(Information, 4, 0)
        Debuggingbox.addWidget(self.InformationEdit, 4, 1, 4,1)
        self.setLayout(Debuggingbox)

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
        fileName1 = QFileDialog.getOpenFileName(self,"Image files (*.jpg *.gif *.png)", "选取文件")
        global path,file_name
        path = fileName1[0]
        f = QFileInfo(path)
        file_name = f.fileName()
        self.open_path_text.setText(file_name)



    def savefile(self):
        global Name,packageName,Vsersion,info
        Name= self.open_path_text.text()
        packageName = self.PackageNameEdit.text()
        Vsersion= self.VsersionEdit.text()
        info= self.InformationEdit.toPlainText()
        print(Name,packageName,Vsersion,info)

        "调用paramiko连接服务器并保存"
        if not all ([Name,packageName,Vsersion,info]):
            QMessageBox.warning(self, "警告", "请查看相关信息是否未填写！")
        else:
            ex.Putserver()
            ex.dboperation()
            self.open_path_text.clear()
            self.PackageNameEdit.clear()
            self.VsersionEdit.clear()
            self.InformationEdit.clear()

    def Putserver(self):
        # 实例化一个transport对象
        trans = paramiko.Transport(('120.24.239.10', 22))
        # 建立连接
        trans.connect(username='root', password='nBc3wGh6w9j')
        ssh = paramiko.SSHClient()
        ssh._transport = trans
        # 实例化一个 sftp对象,指定连接的通道
        sftp = paramiko.SFTPClient.from_transport(trans)
        sftp.put(localpath='{}'.format(path), remotepath='/root/{}'.format(file_name))

    def dboperation(self):
        currenttime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 打开数据库连接
        db = pymysql.connect(host='rds0cxlu1x8n4a289397132.mysql.rds.aliyuncs.com',
                             user='ubodydbuser',
                             passwd='k3n9P_8Knaf',
                             db='ubody_organization',
                             charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        sql = "insert into app_version(av_url,av_name,av_version,av_desc,av_status,av_addtime,av_edittime,av_admin_id) values(%s,%s,%s,%s,%s,%s,%s)"
        val= ('http://api.ubody.net/apk/'+file_name,Name,Vsersion,info,1,currenttime,currenttime,0)
        try:
            cursor.execute(sql,val)
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()

    #删除按钮
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
