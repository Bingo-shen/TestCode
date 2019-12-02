#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-23 12:21
# @Author : shenqiang
# @Software: PyCharm

import  unittest
from selenium import webdriver


class BaiduStart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()











