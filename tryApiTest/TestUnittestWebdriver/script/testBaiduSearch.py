#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-25 10:23
# @Author : shenqiang
# @Software: PyCharm

from TestUnittestWebdriver.script.BaiduStart import *

class Baidu_search(BaiduStart):

    @unittest.skip("新闻加载时间比较长，暂时跳过")
    def test_001_baidu_new(self):
        '''首页：点击新闻是否可以跳转'''
        self.driver.find_element_by_link_text("新闻").click()
        self.assertEqual(self.driver.current_url,"http://news.baidu.com/")
        self.driver.back()

    @unittest.skip("地图加载时间比较长，暂时跳过")
    def test_002_baidu_map(self):
        '''首 页：点击地图是否可以跳转'''
        self.driver.find_element_by_link_text("地图").click()
        self.assertEqual(self.driver.current_url,"https://map.baidu.com/@13523265.31,3641114.64,12z")
        self.driver.back()

    def test_003_baidu_searchAbled(self):
        '''测试输入框是否可以输入信息'''
        so = self.driver.find_element_by_id("kw")
        self.assertTrue(so.is_enabled())

    def test_004_baidu_search(self):
        '''首页：搜索'无涯'是否成功跳转'''
        search = self.driver.find_element_by_id("kw")
        search.send_keys("无涯")
        self.driver.find_element_by_id("su").click()
        '''只要我们在input表单中输入内容，他都在value的属性里面，通过元素定位是找不到这个属性的'''
        self.assertEqual(search.get_attribute("value"),"无涯")















