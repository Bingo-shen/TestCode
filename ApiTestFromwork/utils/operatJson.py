#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import json
from  utils.public import  *
from  utils.operatExcel import OperatExecl

class OperatJson:

    def __init__(self):
        '''使用构造函数，实例化OperatExecl()'''
        self.excel = OperatExecl()

    def getReadJson(self):
        '''读取json文件的内容'''
        with open(data_dir(fileName='jsonData.json'),encoding='gbk') as file:
            return json.load(file)

    def getRequestsData(self,row):
        '''
        self.excel.getExcelRequest_data(row=row)方法确定request_data =3，为第三列，其中row传递的是行数
        '''
        return json.dumps(self.getReadJson()[self.excel.getExcelRequest_data(row=row)])

