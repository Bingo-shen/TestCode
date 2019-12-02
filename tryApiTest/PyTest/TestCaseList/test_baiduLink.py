#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import unittest
from time import sleep

from  selenium import webdriver
'''百度超链接跳转和搜索测试'''
class BaiduTest(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls.driver = webdriver.Chrome()
            cls.driver.get('https://www.baidu.com/')
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(60)


        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()


        def test_001_BaiduNews(self):
            '''获取百度新闻地址'''
            self.driver.find_element_by_link_text('新闻').click()
            self.assertEqual(self.driver.current_url,'http://news.baidu.com/')
            self.driver.back()
            sleep(3)

        @unittest.skip('进入百度地图部分，无法返回所以跳过')
        def test_002_BaiduMap(self):
            '''获取百度地图地址'''
            self.driver.find_element_by_link_text('地图').click()
            self.assertEqual(self.driver.current_url,'https://map.baidu.com/')
            sleep(5)
            self.driver.back()

        def test_003_BaiduSearch(self):
            '''获取百度搜索是否可以点击'''
            so = self.driver.find_element_by_id('kw')
            self.assertTrue(so.is_enabled())
            sleep(3)

        def test_004_BaiduSearch_text(self):
            '''获取百度搜索搜索内容是否正确'''
            so = self.driver.find_element_by_id('kw')
            so.send_keys('无涯')
            self.driver.find_element_by_id('su').click()
            self.assertEqual(so.get_attribute('value'),'无涯')
            sleep(3)

if __name__ == '__main__':
    unittest.main(verbosity=2)

