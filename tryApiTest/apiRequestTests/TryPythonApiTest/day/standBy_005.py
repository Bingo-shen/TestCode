#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-22 20:31
# @Author : shenqiang
# @File : standBy_005.py
# @Software: PyCharm

import unittest
from selenium import webdriver

class Stand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Chrome()
        cls.dirver.maximize_window()
        cls.dirver.get("https://www.baidu.com/")
        cls.dirver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.dirver.quit()

    def suite(self):
        '''加载整个测试类'''
        suite = unittest.TestLoader().loadTestsFromTestCase(F6)
        return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(F6.suite())