#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang


def test_baidu_url(driver,init):
   assert  driver.current_url=='https://www.baidu.com/'

class TestUi(object):
	def test_baidu_title(self,driver,init):
		assert driver.title=='百度一下，你就知道'
