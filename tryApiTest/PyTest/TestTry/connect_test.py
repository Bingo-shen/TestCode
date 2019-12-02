#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import unittest
from time import sleep
from selenium import webdriver

class BaiduTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.diver = webdriver.Chrome()
        cls.diver.maximize_window()
        cls.diver.implicitly_wait(50)
        cls.diver.get('https://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.diver.quit()


    def test_baidu_001(self):
        '''测试点击新闻后是否会跳转'''
        self.diver.find_element_by_link_text('新闻').click()
        self.diver.back()
        sleep(3)

    def test_baidu_002(self):
        '''测试点击贴吧后是否会跳转'''
        self.diver.find_element_by_partial_link_text('贴吧').click()
        self.diver.back()
        sleep(3)

    def test_baidu_003(self):
        '''测试点击地图后是否会跳转'''
        self.diver.find_element_by_partial_link_text('地图').click()
        # self.diver.back()
        sleep(5)

'''用例执行次数'''
# class   TestTimes(BaiduTest):
#
#         @classmethod
#         def TryTimes(cls):
#             times = 3
#             for i in  range(times):
#                 cls.run(i)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    '''调用TestSuite来执行test顺序'''
    suite = unittest.TestSuite()
    suite.addTest(BaiduTest)
    unittest.TextTestRunner(verbosity=2).run()





