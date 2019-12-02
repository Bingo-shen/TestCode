#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-22 23:07
# @Author : shenqiang
# @File : TestCases.py
# @Software: PyCharm

from selenium import webdriver
import unittest

class baiDuLinkForward(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Chrome()
        cls.dirver.get("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.dirver.quit()

    def test_001_baidu_new(self):
        '''测试百度新闻跳转正常'''
        self.dirver.find_element_by_link_text("新闻").click()
        self.assertEqual(self.dirver.current_url,"http://news.baidu.com/")
        self.dirver.back()

    def test_002_baidu_map(self):
        '''测试百度地图跳转正常'''
        self.dirver.find_element_by_link_text("地图").click()
        self.assertEqual(self.dirver.current_url,"https://map.baidu.com")
        self.dirver.back()

if __name__ == '__main__':
    unittest.main(verbosity=2)

