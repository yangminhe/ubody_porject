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
import paramiko

# 引用日志配置
logging.config.dictConfig(settings.LOGGING)
# 引用日志记录器
loggers = logging.getLogger('log')


class Putserver():
    # 实例化一个transport对象
    trans = paramiko.Transport(('120.24.239.10', 22))
    # 建立连接
    trans.connect(username='root', password='nBc3wGh6w9j')

    def connection(self):
        # # 将sshclient的对象的transport指定为以上的trans
        ssh = paramiko.SSHClient()
        ssh._transport = Putserver.trans
        # 执行命令，和传统方法一样
        stdin, stdout, stderr = ssh.exec_command('pwd')
        print(stdout.read().decode('utf-8'))

    def putconnet(self):
        # 实例化一个 sftp对象,指定连接的通道
        sftp = paramiko.SFTPClient.from_transport(Putserver.trans)
        # 发送文件
        path1 = open("../Qt_pratice/path_load", "r+")
        Fpath = path1.read()
        #存储地址
        Files = open("../Qt_pratice/file_os", "r+")
        Fname = Files.read()
        sftp.put(localpath='{}'.format(Fpath), remotepath='/root/{}'.format(Fname))
        # 下载文件`
        # sftp.get(remotepath, localpath)
        # 关闭连接
        # trans.close()


if __name__ == '__main__':
    start = Putserver()
    # start.connection()
    start.putconnet()
