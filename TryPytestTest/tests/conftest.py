#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import  pytest
from selenium import  webdriver

@pytest.fixture(scope='session')
def driver():
   return webdriver.Chrome()

@pytest.fixture(scope='session')
def init(driver):
   driver.maximize_window()
   driver.get('http://www.baidu.com')
   driver.implicitly_wait(30)
   yield
   driver.quit()