#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
from base.Test_Head import *

class BaiduTitle(TestHead):

    def test_BaiduTitleTest(self):
        self.assertEqual(self.diver.title,'百度一下，你就知道')

    def test_Baidukw(self):
        so = self.diver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled(),True)

    def test_BaiduIn(self):
        # so = self.diver.find_element_by_id('kw')
        '''断言haha是不是浏览器标题'''
        try:
            self.assertIn('haha',self.diver.title)
        except Exception as e:
            print('error is {0}'.format(e.args))

if __name__ == '__main__':
    unittest.main(verbosity=2)








