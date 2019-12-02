#!/user/bin/env python
#coding:utf-8

#Author:shenqiang

from selenium import webdriver

'''
函数的调用必须要带有实际参数，不然会报错
'''
# def f1(name):
#     print(name)
# f1()

# def f1(name):
#     print('username is ',name)
# f1('name')
#
# '''
# 动态参数：
# *args -->数据类型是元祖
# **kwargs -->数据类型是字典
# '''
#
# def T1(*args):
#     print(args,type(args))
# T1()
#
# def T2(**kwargs):
#     print(kwargs,type(kwargs))
# T2()
#
# def T3(name,age,sex,*args):
#     print('用户信息：',name,age,sex,args)
# T3('shenqiang',12,'man','180','nanjing')
#
# def T4(name1,age1,sex1,**kwargs):
#     print('用户信息：',name1,age1,sex1,kwargs)
# T4('shenqiang',12,'man',phone='180',address='nanjing')
#
# # 设置万能参数
# def T5(*args,**kwargs):
#     print(args,kwargs)
# T5()
# T5(2)
# T5('admin')
# T5([1,2])
# T5(address='nanjing')

'''
全局变量和局部变量

'''
# 全局变量
name = 'shenqiang'

def f1():
    print(name)

def f2():
    # global对局部变量进行修改
    global name
    # 局部变量
    name = 'xiaoqiang'
    print(name)

f1()
f2()



