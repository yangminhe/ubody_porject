# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ddt_test
   Description :
   Author :       杨敏和
   date：         2020/2/8 19:03
-------------------------------------------------
   Change Activity:
                   2020/2/8:
-------------------------------------------------
"""
import logging.config
import os
from blog.object import settings
import unittest
from ddt import ddt,data,file_data,unpack
from selenium import webdriver
import time
#引用日志配置
logging.config.dictConfig(settings.LOGGING)
#引用日志记录器
loggers = logging.getLogger('log')


# @ddt

# class MyTestDdt(unittest.TestCase):
#     def setUp(self):
#         print('start')
#     @data(a,b,30)#使用data传参数给测试用例
#     def test_one(self,value):
#         print(f'the @data number is :{value}')
#
#     def tearDown(self):
#         print('end')

# class MyTestDdt(unittest.TestCase):
#     def setUp(self):
#         print('start')
#
#     @data((1,2),(4,5)) #元组
#     @unpack #分解
#     def test_one(self,value1,value2):
#         print(f'the @data number is :{value1,value2}')
#
#     def tearDown(self):
#         print('end')



def testdata():
    '''测试数据'''
    return [('', '', '请输入邮箱名'), ('', '123456', '请输入邮箱名'),
            ('123456', '', '您输入的邮箱名格式不正确')]

@ddt
class MyMailLogin(unittest.TestCase):
    def setUp(self):
        self.url = 'https://mail.sina.com.cn/'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)

    @data(*testdata()) #这里加*后会将返回数据分为一个个的元组
    @unpack
    def test_login(self,username,password,result):
        '''测试邮箱登录'''
        self.driver.find_element_by_id('freename').clear()
        time.sleep(2)
        self.driver.find_element_by_id('freename').send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_id('freepassword').clear()
        time.sleep(2)
        self.driver.find_element_by_id('freepassword').send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(2)
        freeError = self.driver.find_element_by_xpath('//div[@class="freeError"]//span').text
        time.sleep(2)
        self.assertEqual(freeError,result)

    def tearDown(self):
        self.driver.quit()
"""
verbosity是一个选项,表示测试结果的信息复杂度，有0、1、2 三个值
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
并且 你在命令行里加入不同的参数可以起到一样的效果
加入 --quiet 参数 等效于 verbosity=0
加入--verbose参数等效于 verbosity=2
什么都不加就是 verbosity=1
"""
if __name__ == '__main__':
    unittest.main(verbosity=2)



