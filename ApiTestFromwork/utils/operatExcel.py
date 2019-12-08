#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import xlrd
from  utils.public import  *
from  utils.excelData import *

class OperatExecl:
    '''操作excelDatas表'''

    def getExcel(self):
        '''获取excel的sheet页'''
        Excel= xlrd.open_workbook(data_dir('data',"excelDatas.xls"))
        sheet = Excel.sheet_by_index(0)
        return sheet

    def getExcelRow(self):
        '''获取excel的行数'''
        return self.getExcel().nrows

    def getExcelRowCel(self,row,cel):
        '''获取单元格的内容'''
        return self.getExcel().cell_value(row,cel)

    def getExcelCaseID(self,row):
        '''获取测试ID'''
        return self.getExcelRowCel(row,CaseID())

    def getExcelUrl(self,row):
        '''获取请求地址'''
        return self.getExcelRowCel(row,Url())

    def getExcelRequest_data(self,row):
        '''获取请求参数'''
        return self.getExcelRowCel(row,Request_data())

    def getExcelExceptResult(self, row):
        '''获取期望结果'''
        return self.getExcelRowCel(row, ExceptResult())

    def getExcelActualResult(self, row):
        '''获取实际结果'''
        return self.getExcelRowCel(row, ActualResult())

