#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-22 22:05
# @Author : shenqiang
# @File : Unit_test007.py
# @Software: PyCharm

from TryPythonApiTest.day.standBy_005 import *


class baidu(Stand):

    def test_001(self):
        self.assertEqual(self.dirver.title,"百度一下，你就知道")

    def test_002(self):
        so = self.dirver.find_element_by_id("kw")
        self.assertTrue(so)

    def test_003(self):
        try:
            sp = self.dirver.find_element_by_id("w")
            self.assertFalse(sp)
        except Exception as a:
            print(a.args)

    def test_004(self):
        self.assertIn('百度',self.dirver.title)

if __name__ == '__main__':
    baidu()








