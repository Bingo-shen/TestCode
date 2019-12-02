#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-22 20:24
# @Author : shenqiang
# @File : Unit_test005.py
# @Software: PyCharm
from TryPythonApiTest.day.standBy_005 import *

class F6(Stand):

    def test_001_baiduSearch(self):
        self.dirver.find_element_by_id("kw").send_keys('webdriver')

















