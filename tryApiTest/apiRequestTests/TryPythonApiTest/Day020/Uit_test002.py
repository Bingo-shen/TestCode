#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-22 14:12
# @Author : shenqiang
# @File : Uit_test002.py
# @Software: PyCharm

import unittest

class F1(unittest.TestCase):

    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    def test_001(self):
        print("test1")

    def test_002(self):
        print("test2")

    def test_003(self):
        self.assertEqual(1,"1")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_002)
    suite.addTest(test_001)
    suite.addTest(test_003)
    unittest.TextTestRunner(verbosity=2).run(suite)


