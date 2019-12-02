#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import requests
from  utils.excelData import getHeadersValues
from  utils.operatExcel import OperatExecl
from  utils.operatJson import OperatJson


class Method:
    '''封装post方法'''
    def __init__(self):
        '''实例化OperatExecl、OperatJson'''
        self.OperatExecl = OperatExecl()
        self.OperatJson = OperatJson()

    def post(self,row):
        try:
            '''调用封装好的url和data方法'''
            r = requests.post(
                url= self.OperatExecl.getExcelUrl(row=row),
                data= self.OperatJson.getRequestsData(row=row),
                headers = getHeadersValues(),
                timeout = 6
            )
            return r
        except Exception:
            raise RuntimeError('接口请求发生未知的错误')

    def sessionid(self,row):
        try:
            '''调用封装好的url和data方法'''
            sessionId = requests.Session()
            r = sessionId.post(
                url=self.OperatExecl.getExcelUrl(row=row),
                data=self.OperatJson.getRequestsData(row=row),
                headers=getHeadersValues(),
                timeout=6
            )
            return r
        except Exception:
            raise RuntimeError('接口请求发生未知的错误')

    def postData(self,row,data):
        try:
            '''调用封装好的url和data方法'''
            r = requests.post(
                url= self.OperatExecl.getExcelUrl(row=row),
                data= data,
                headers = getHeadersValues(),
                timeout = 6
            )
            return r
        except Exception:
            raise RuntimeError('接口请求发生未知的错误')

