#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import xlrd
import os
from xlutils.copy import copy



'''拿到文件的路径'''
def base_path(filename = None):
    return os.path.join(os.path.dirname(__file__),filename)

'''打开文件'''
work = xlrd.open_workbook(base_path('tryExeclRead.xls'))
'''把文件内存存在一个变量里'''
file_content = copy(work)
'''拿到文件需要改写的sheet页'''
file = file_content.get_sheet(0)
# print(file_content)
'''定位文件位置写入内容'''
file.write(9,3,'沈强')
'''保存文件'''
file_content.save(base_path('tryExeclRead.xls'))



# '''以下标或者sheet名取对应的哪页'''
# sheet = work.sheet_by_index(0)
# # sheet = work.sheet_by_name()
#
# '''查看文件有多少行'''
# print(sheet.nrows)
#
# '''获取单元格内容,第10行，第3列'''
# print(sheet.cell_value(9,2))




