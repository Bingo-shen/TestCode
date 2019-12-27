#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

def test_baidu_so(driver,init):
	so=driver.find_element_by_id('kw')
	so.send_keys('bingo')
	assert so.get_attribute('value')=='bingo'


