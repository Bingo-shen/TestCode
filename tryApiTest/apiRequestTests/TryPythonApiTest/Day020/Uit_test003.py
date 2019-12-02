#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-22 14:54
# @Author : shenqiang
# @File : Uit_test003.py
# @Software: PyCharm

'''使用浏览器打开'''
import unittest
from selenium import webdriver
from time import sleep

class F2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Chrome()
        cls.dirver.maximize_window()
        cls.dirver.get("https://www.baidu.com/")
        cls.dirver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.dirver.quit()

    '''百度首页链接测试'''
    def test_001_baidu_news(self):
        '''首页链接测试：验证新闻的链接'''
        self.dirver.find_element_by_link_text("新闻").click()
        sleep(2)
        self.dirver.back()

    def test_002_baidu_map(self):
        '''首页链接测试：验证贴吧的链接'''
        self.dirver.find_element_by_link_text("贴吧").click()
        sleep(2)
        self.dirver.back()

    '''百度首页搜索测试'''
    def test_003_baidu_search(self):
        '''首页搜索：搜索webdirver'''
        self.dirver.find_element_by_id('kw').send_keys('webdirver')
        self.dirver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)


