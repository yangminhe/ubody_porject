from django.db import models

# Create your models here.
# import logging
import os
import logging.config

#返回当前文件所在的绝对路径：models.py文件路径：注意这里使用了file等于当前文件
cur_path = os.path.dirname(os.path.realpath(__file__))

#在上面一层的路径中使用dirname返回上一层路径创建logs目录
logfile_dir = os.path.join(os.path.dirname(cur_path),'logs') # 存放log文件的目录

#下面使用变量定义一个log文件名，然后使用join函数把目录和文件合成一个路径
logfile_name = 'all2.log' # log文件名
logfile_path = os.path.join(logfile_dir, logfile_name)


#判断日志目录是否存在，不存在则自动创建
if not os.path.exists(logfile_dir):
    os.mkdir(logfile_dir)

#配置输出日志格式一种定义方式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
#配置输出日志格式二种定义方式
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
#配置输出日志格式三种定义方式
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

"""
logging.config.dictConfig，json的字典配置模式进行日志配置
1、定义了一个lggers，记录器
2、定义一个handlers，处理器
3、没有定义filters，过滤器
4、定义一个formatters,格式化器
"""
LOGGING_DIC = {
    'version': 1, #版本信息
    'disable_existing_loggers': False,
     #定义格式化器
    'formatters': {
#日志格式赋值stanard
        'standard': {
            'format': standard_format #调用第一种日志格式
        },
        #日志格式赋值simple
        'simple': {
            'format': simple_format #调用第二种日志格式
        },
    },
    'filters': {},
    'handlers': {
            #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler', # 打印到屏幕
            'formatter': 'simple'
        },
            #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler', # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path, # 日志文件
            'maxBytes': 102410245, # 日志大小 5M
            # 'interval':'D',   #定义创建日志时间，D表示每天,不同名的每天都会自动创建文件，Logger会自动重建文件，若这个文件跟之前的文件有重名，则会自动覆盖掉以前的文件
            'backupCount': 5,  #只保留5份日志文件，超过则删除
            'encoding': 'utf-8', # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(name)拿到的logger配置
        '': {
            'handlers': ['default', 'console'], # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True, # 向上（更高level的logger）传递
        },
    },
}
#定义函数，对日志的所有配置和实例定义，还有监控logger的运行状态
def load_my_logging_cfg(msg):
    logging.config.dictConfig(LOGGING_DIC) # 导入上面定义的logging配置
    logger = logging.getLogger('name') # 生成一个log实例
    logger.info(msg) # 记录该文件的运行状态

if __name__ == '__main__':
    load_my_logging_cfg()


