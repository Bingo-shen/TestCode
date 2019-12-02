#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-22 17:19
# @Author : shenqiang
# @File : Uit_test004.py
# @Software: PyCharm

import unittest

class F6(unittest.TestCase):

    @classmethod
    def setUp(cls):
        pass

    @classmethod
    def tearDown(cls):
        pass

    def test_001(self):
        print('test1')

    def test_002(self):
        print('test2')

    def suite(self):
        suite = unittest.TestLoader().loadTestsFromModule('模块名.py')
        return suite

if __name__ == '__main__':
    '''按照模块运行'''
    # suite = unittest.TestSuite(unittest.makeSuite(F6))


    '''加载整个测试类'''
    # suite  = unittest.TestLoader().loadTestsFromTestCase(F6)

    '''加载整个模块'''

    unittest.TextTestRunner(verbosity=2).run(F6.suite())






