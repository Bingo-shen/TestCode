#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-25 14:55
# @Author : shenqiang
# @File : BaiduEnd.py
# @Software: PyCharm
import os
from TestUnittestWebdriver.script.testBaiduSearch import *
import HTMLTestRunner
import time


def DiscoverTest():
    '''批量testcase执行'''
    suite = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),
        pattern="test*.py")
    return suite

def getNowTime():
    '''测试报告加入当前时间'''
    return time.strftime("%Y-%m_%d %H_%M_%S",time.localtime(time.time()))

def run():
    '''生成测试报告'''
    file = os.path.join(os.path.dirname(__file__), 'report', getNowTime()+' testreport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(file, 'wb'),
        title='百度首页自动化测试',
        description='百度首页自动化测试详细信息').run(DiscoverTest())

if __name__ == '__main__':
    run()