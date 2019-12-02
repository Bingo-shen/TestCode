#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang
from  utils.operatExcel import OperatExecl

class IsContent:
    '''封装：依据某行判断预期结果与实际结果是否一致'''
    def __init__(self):
        '''实例化OperatExecl'''
        self.excel = OperatExecl()

    def isContent(self,row,str2):
        '''判断excel文档的预期结果和实际结果是否一致'''
        if self.excel.getExcelExceptResult(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag