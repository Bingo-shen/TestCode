#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-06 17:31
# @Author : shenqiang
# @File : TryExcpt.py
# @Software: PyCharm

def  test(a,b):
    print(a/b)

try:
    test(1,0)
except ZeroDivisionError as  e:
    print(e.args)

