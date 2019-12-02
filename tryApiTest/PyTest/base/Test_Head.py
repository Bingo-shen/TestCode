#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
import unittest
from selenium import webdriver


class TestHead(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.diver = webdriver.Chrome()
        cls.diver.maximize_window()
        cls.diver.implicitly_wait(30)
        cls.diver.get('https://www.baidu.com')


    @classmethod
    def tearDownClass(cls):
        cls.diver.quit()

# print(os.path.dirname(__file__))