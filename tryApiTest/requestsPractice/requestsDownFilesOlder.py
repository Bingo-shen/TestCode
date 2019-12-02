#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import requests

'''
1.按照流的方式进行下载
2.下载好后写入文件中
'''

'''登录用户数据'''
data={"username":"lyfadmin","password":"liuhaijun123456","type":1}

'''下载地址和文件名'''
download_path = '/Users/apple/Documents/TestCode/loadTest.xlsx'


def getLoginHeaders():
    '''获取登录用的headers'''
    headers = {'Content-Type':'application/json;charset=UTF-8','Referer':'http://lyfadmin.edu.laiyifen.com/plugins/platform-include/views/login.html',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
               }
    return headers


def  urlTest():
    '''
    实例化session对象
    登陆return Session
    '''
    sessionID = requests.Session()
    '''直接调用session'''
    sessionID.post(url='http://lyfadmin.edu.laiyifen.com/ouser-web/mobileLogin/login.do',
                      json=data,
                      headers=getLoginHeaders()
                      )
    return sessionID

def getCouponFile():
    '''
    调用下载文件的接口，实现文件下载
    '''
    getCouponFile = urlTest().get('http://lyfadmin.edu.laiyifen.com/promotion-static/template/coupon.xlsx',headers=getLoginHeaders(),stream=True)
    '''判断是否请求成功'''
    if getCouponFile.status_code == 200:
        '''以write权限open文件'''
        with open(download_path,'wb') as file:
            '''以1kb写入下载内容'''
            for chunk in getCouponFile.iter_content(chunk_size=1024):
                file.write(chunk)
    return

getCouponFile()