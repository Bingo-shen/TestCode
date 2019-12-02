#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

from time import sleep
from base.Test_Head import *

class Baidu_Search(TestHead):


    def test_001_link(self):
        self.diver.find_element_by_id('kw').send_keys('无涯')
        self.diver.back()
        sleep(5)

    def test_002_News(self):
        self.diver.find_element_by_link_text('新闻').click()
        sleep(5)

    '''静态方法分离'''
    @staticmethod
    def suite():
        suite = unittest.TestLoader().loadTestsFromModule()
        return suite

if __name__ == '__main__':
    '''执行某个模块的测试'''
    unittest.TextTestRunner(verbosity=2).run()





