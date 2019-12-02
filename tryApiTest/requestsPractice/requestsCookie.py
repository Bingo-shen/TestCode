#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-26 11:30
# @Author : shenqiang
# @File : requestsCookie.py
# @Software: PyCharm

'''
注意区分：http协议和websocket协议的区别
http是建立一次链接，当然也可以通过ajax进行轮询，但是效率比较低，会有超时的风险
websocket是和服务器建立双向的持久性链接
'''
import json
import requests

def gitHeaders():
    headers = {'Content-Type':'application/json;charset=UTF-8','Referer':'http://lyfadmin.edu.laiyifen.com/plugins/platform-include/views/login.html'}
    return headers

data={"username":"lyfadmin","password":"liuhaijun123456","type":1}

'''登陆return cookies'''
def  urlTest():
    r = requests.post(url='http://lyfadmin.edu.laiyifen.com/ouser-web/mobileLogin/login.do',
                      json=data,
                      headers=gitHeaders()
                      )
    return r.cookies

'''调用cookies'''
def getUrlTest():
    get = requests.get(url='http://lyfadmin.edu.laiyifen.com/guide/getBackGuideSetting.do',
                       cookies = urlTest())
    print(json.dumps(get.json(),indent=True,ensure_ascii=False))

getUrlTest()

# print(urlTest())


