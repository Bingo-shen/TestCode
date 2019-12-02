#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import unittest
from time import sleep

from selenium import webdriver


class Baidu_link(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.diver = webdriver.Chrome()
        cls.diver.maximize_window()
        cls.diver.implicitly_wait(30)
        cls.diver.get('https://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.diver.quit()

    def test_baidu_news(self):
        self.diver.find_element_by_link_text('新闻').click()
        sleep(2)

    def test_baidu_photos(self):
        self.diver.find_element_by_partial_link_text('贴吧').click()


class Baidu_Search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.diver = webdriver.Chrome()
        cls.diver.maximize_window()
        cls.diver.implicitly_wait(30)
        cls.diver.get('https://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.diver.quit()

    def test_link(self):
        self.diver.find_element_by_id('kw').send_keys('无涯')
        sleep(5)

if __name__ == '__main__':
    '''执行某个模块的测试'''
    suite = unittest.TestLoader().loadTestsFromModule('U_test.py')
    unittest.TextTestRunner(verbosity=2).run()







