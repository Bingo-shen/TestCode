#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang
import csv

'''读取csv文件的方法'''
def ReadCsvlist():
    '''方法一:列表方式取数据'''
    '''通过列表提取csv文件'''
    with open('csvTestFile.csv') as file:
        '''reader是csv的迭代器'''
        reader = csv.reader(file)
        '''跳过首行'''
        next(reader)
        '''列表推倒式'''
        db =  [item for item in reader]
        return db

print(ReadCsvlist(),type(ReadCsvlist()))

#     '''方法二：字典的格式输出csv文档内容'''
#     with open('csvTestFile.csv',encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for item in reader:
#             print(dict(item))
#
# ReadCsvlist()

