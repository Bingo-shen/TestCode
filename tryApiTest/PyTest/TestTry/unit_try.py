#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import unittest


class F1(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_01(self):
        print('test_01')

    def test_02(self):
        print('test_02')

    def test_03(self):
        print('test_03')

if __name__ == '__main__':
    unittest.main(verbosity=2)


