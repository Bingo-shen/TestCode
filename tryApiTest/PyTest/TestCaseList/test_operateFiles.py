#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
import time
import unittest
import os
import HTMLTestRunner

'''
如果是在python2中，一定要加如下代码，如果不加会出现中文enicode error的错误信息
import sys
reload（sys）
sys.setdefaultencoding('utf-8')
'''

'''文件调用方法'''
def OperateFiles():
    suite = unittest.TestLoader().discover(
    start_dir=os.path.dirname(__file__),
    pattern='test_*.py',
    top_level_dir=None)
    return suite

'''文件执行方法'''
def Run():
    # unittest.TextTestRunner(verbosity=2).run(OperateFiles())
    file = os.path.join(os.path.dirname(__file__),'report',getNewTime()+'testReport.html')
    HTMLTestRunner.HTMLTestRunner(
        stream=open(file,'wb'),
        title='UI自动化测试',
        description='中台UI自动化测试详细信息').run(OperateFiles())

def getNewTime():
    return time.strftime('%Y_%m_%d %H_%M_%S',time.localtime(time.time()))

if __name__ == '__main__':
    Run()





