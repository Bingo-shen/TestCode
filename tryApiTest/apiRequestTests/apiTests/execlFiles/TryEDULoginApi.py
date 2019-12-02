#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
import json
import requests

def gitHeaders():
    headers = {'Content-Type':'application/json;charset=UTF-8','Referer':'http://lyfadmin.edu.laiyifen.com/plugins/platform-include/views/login.html'}
    return headers

data={"username":"lyfadmin","password":"liuhaijun123456","type":1}

'''登陆return cookies'''
def  urlTest():
    '''实例化session对象'''
    sessionID = requests.Session()
    '''直接调用session'''
    sessionID.post(url='http://lyfadmin.edu.laiyifen.com/ouser-web/mobileLogin/login.do',
                      data=json.dumps(data),
                      headers=gitHeaders()
                      )
    return sessionID

'''调用session'''
def getUrlTest():
    get = urlTest().get(url='http://lyfadmin.edu.laiyifen.com/guide/getBackGuideSetting.do')
    print(get.text)

getUrlTest()

