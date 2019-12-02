#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
import unittest
# from selenium import  webdriver

class F5(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUp')

    @classmethod
    def tearDownClass(cls):
        print('tearDown')

    def test_001(self):
        print('Test_001')

    def test_002(self):
        print('Test_002')


'''调能用TestSute前，加载TestClass'''
if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.TestLoader(F5))
    unittest.TextTestRunner(verbosity=2).run(suite)
    # suite = unittest.TestSuite(F5)
    # unittest.main()


