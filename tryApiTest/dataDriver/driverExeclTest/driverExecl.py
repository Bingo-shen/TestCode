#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

'''xlrd写入文件，同时清空原文件,一般这种方法只用来读'''

import xlrd
import os
from xlutils.copy import copy

# '''拿到文件的路径'''
# def base_path(filename = None):
#     return os.path.join(os.path.dirname(__file__),filename)
#
# '''读取文件内容'''
# work = xlrd.open_workbook(base_path('execlTestFile.xls'))
#
# '''以下标或者sheet名取对应的哪页'''
# sheet = work.sheet_by_index(0)
# # sheet = work.sheet_by_name()
#
# '''查看文件有多少行'''
# print(sheet.nrows)
#
# '''获取单元格内容,第3行，第3列'''
# print(sheet.cell_value(2,2))

'''execl文件的修改'''

'''难道文件的路径'''

def driPathFiles(files):
    return os.path.join(os.path.dirname(__file__),files)

'''找到xls对象'''
work = xlrd.open_workbook(driPathFiles('execlTestFile.xls'))

'''copy文件内容'''
old_content = copy(work)

'''找到文件的sheet页'''
file = old_content.get_sheet(0)

'''写入修改的信息'''
file.write(2,2,'沈强')

'''保存文件重新命名'''
old_content.save(driPathFiles('execlTestFile.xls'))


