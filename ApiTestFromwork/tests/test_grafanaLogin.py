#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import unittest
from base.method import Method
from base.isAssert import IsContent
from pages.grafana import setJsonData,setNameLoginOrEmail
import json

class Grafana(unittest.TestCase):

    def setUp(self):
        '''实例化Method'''
        self.obj = Method()
        self.Assert = IsContent()

    def statusCode(self,r):
        '''断言协议状态码'''
        self.assertEqual(r.status_code,200)
        # 这个部分需要替换成code业务状态码，一般为{'code':'0'}
        # self.assertEqual(r.json()['message'],"Logged in")

    def baseAssert(self,r,row):
        '''基础断言'''
        self.statusCode(r=r)
        '''json字符串内参数断言'''
        self.assertTrue(self.Assert.isContent(row=row, str2=r.text))

    def test_001_login(self):
        '''测试登录Grafana'''
        r = self.obj.post(1)
        self.baseAssert(r=r,row=1)

    def test_002_mail(self):
        '''测试email是动态参数'''
        r = self.obj.postData(row=1,data=json.dumps(setJsonData('111')))
        self.baseAssert(r=r,row=1)

    def test_003_invites(self):
        '''测试增加用户名为shen的管理员'''
        r = self.obj.postData(row=2,data=json.dumps(setNameLoginOrEmail(name="shen",loginOrEmail="shen")))
        self.baseAssert(r=r,row=2)

if __name__ == '__main__':
    unittest.main(verbosity=2)

