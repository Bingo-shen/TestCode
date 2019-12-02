#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import unittest
from time import sleep

from selenium import webdriver

'''
调用类方法，只执行一次setup和teardown
self.diver.back() 每次动作后返回到操作前
'''
class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.diver = webdriver.Chrome()
        cls.diver.maximize_window()
        cls.diver.implicitly_wait(30)
        cls.diver.get('https://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.diver.quit()


    def test_001_baidu_news(self):
        '''测试点击新闻后是否会跳转'''
        self.diver.find_element_by_link_text('新闻').click()
        self.diver.back()
        sleep(2)

    def test_002_baidu_photos(self):
        '''测试点击新闻后是否会跳转'''
        self.diver.find_element_by_partial_link_text('贴吧').click()
        self.diver.back()
        sleep(2)

    def test_003_baidu_login(self):
        '''测试点击新闻后是否会跳转'''
        self.diver.find_element_by_link_text('学术').click()
        sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)







