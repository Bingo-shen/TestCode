#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-15 20:42
# @Author : shenqiang
# @File : 11.py
# @Software: PyCharm
users =[{'name':'py01','pwd':'123'},
        {'name':'py02','pwd':'123'},
        {'name':'py03','pwd':'123'},
        {'name':'py04','pwd':'123'}]

for item in users:
    print(item)
    #判断字典的name键对应的值是否为py03
    if item['name'] =='py03':
        print('找到了该用户')
        continue

    print(f'比对完用户{item}')
else:
    print(f'没有找到py03这个用户')





