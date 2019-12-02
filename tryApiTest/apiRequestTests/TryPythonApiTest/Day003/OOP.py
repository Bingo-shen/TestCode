#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-06 21:19
# @Author : shenqiang
# @File : OOP.py
# @Software: PyCharm
#
# '''
# 对象的建立---->是类实例化的过程
# 三个特性：
# 1.对象的句柄--->区分不同的对象
# 2.属性
#     共有属性
#         类属性
#         实例属性
#         局部变量
#
#     私有属性
# 3.方法
# '''
#
# class Person(object):
#     '''类属性'''
#     gongtong = 'China'
#     def __init__(self,name,age):
#         '''实例属性'''
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#     def setName(self,name):
#         self.name = name
#
#     def setAge(self,age):
#         self.age = age
#
# per = Person('shenqiang','28')
# per2 = Person('lll','20')
# print(per.getName(),per.getAge())
#
# per2.setAge('10')
# per2.setName('shen')
# print(per2.getAge(),per2.getName())

# '''构造函数的多个参数'''
# class Person(object):
#     def __init__(self,**kwargs):
#         self.kwargs = kwargs
#
#     def getInfo(self):
#         print(list(self.kwargs.values()))
#
# per = Person(name='shenqiang',age = '28')
# per.getInfo()

# '''
# 满足所有人类的个性，调用万能参数
# 构造函数：即使没写构造函数，类都是有构造函数的
# 一个类可以有多个构造函数，建议一个类只有一个构造函数
# 构造函数用来：
# 1.初始化属性
# '''
# class Persons(object):
#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#     def info(self):
#         print(self.kwargs.values())
#
# per = Persons(name='shenqiang')
# per.info()
#
# per1 = Persons(name='shenqiang',age = 18,address = 'nanjing')
# per1.info()

class Person(object):
    def __init__(self):
        print("我是构造函数")

    def __del__(self):
        print("我是析构函数")

    def info(self):
        print("我是方法")

per = Person()
per.info()



