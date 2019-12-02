#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-22 13:42
# @Author : shenqiang
# @File : Uit_test001.py
# @Software: PyCharm

import unittest

class F1(unittest.TestCase):

    def setUp(self):
        print("准备开始测试")

    def tearDown(self):
        print("测试完成")

    def test_001(self):
        print("test1")

    def test_002(self):
        print("test2")

    def test_003(self):
        print("test3")

if __name__ == '__main__':
    unittest.main(verbosity=2)











