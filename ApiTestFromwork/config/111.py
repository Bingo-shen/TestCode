#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class Factory(object):
    def __init__(self,driver):
        self.driver=driver

    def createDriver(self,driver):
        '''工厂方法'''
        if driver=='web':
            return WebUi(self.driver)
        elif driver=='app':
            return AppUi(self.driver)

class WebDriver():
    def __init__(self,driver):
        self.driver=driver
    def findElement(self,*loc):
        try:
            return WebDriverWait(self.driver,20).until(
                lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print(e.args[0])

    def findElements(self,*loc):
        try:
            return WebDriverWait(self.driver,20).until(
                lambda x:x.find_elements(*loc))
        except NoSuchElementException as e:
            print(e.args[0])

class WebUi(WebDriver):
    def __str__(self):
        return 'WebUi'

class AppUi(WebDriver):
    def __str__(self):
        return 'AppUi'

