from django.shortcuts import render


#导入logging模块的config方法
import logging.config
#引入日志方法文件
from  selenium_porject import models

#直接使用logging模块config方法的dictConfig函数，导入日志文件的logging.config.dictConfig，json配置方法
logging.config.dictConfig(models.LOGGING_DIC)

#生成一个日志生成器，也可以直接注释该记录器，不用该方法，直接使用logging方法直接调用，
logger = logging.getLogger('zb')

#下面是各种日志方法
logging.error('hah')
logging.info("hah")
logging.debug("hah")
logging.warning("hah")
logging.critical("hah")

#这里注意如果使用了记录器logger，则可以使用logger.info的方法使用日志，也可以使用logging.info的方法使用日志
logger.info('11232')