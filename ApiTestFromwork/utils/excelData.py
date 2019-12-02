#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

'''
excelDatas文件的列数处理
'''

class ExcelVariable:
    '''文件列数参数化'''
    CaseID=0
    url=2
    request_data =3
    exceptResult=4
    actualResult=5

'''文件列数函数化：获取列数'''
def CaseID():
    return ExcelVariable.CaseID

def Url():
    return ExcelVariable.url

def Request_data():
    return ExcelVariable.request_data

def ExceptResult():
    return ExcelVariable.exceptResult

def ActualResult():
    return ExcelVariable.actualResult


'''获取请求头'''
def getHeadersValues():
    Headers = {
        'Accept':'application/json, text/plain, */*',
        'Content-Type':'application/json;charset=UTF-8',
        'Referer':'http://192.168.189.189:3000/login',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
        'Content-Length':'53',
        'Cookie':'grafana_session=ce4cbb44c1d0fc0ebfa66f158db5de6c'
    }
    return Headers

