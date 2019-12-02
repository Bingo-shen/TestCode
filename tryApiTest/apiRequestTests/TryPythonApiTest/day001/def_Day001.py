#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-04 15:27
# @Author : shenqiang
# @File : def_Day001.py
# @Software: PyCharm

# def clas(a):
#     print("我在{0}的课程".format(a))
#
# a = input("课程名：")
#
# if a == "网易":
#     clas(a)
# elif a == "51":
#     clas(a)

# '''
# 需求：
# 1.对请求的参数进行ascill码排序
# 2.排序后，对请求的参数进行MD5加密
# '''
# # 排序
# dict1 = {"name":"shenqiang","age":28,"datas":{"name":"shenqiang","age":28}}
#
# def Data(**kwargs):
#     return dict(sorted(kwargs.items(),key=lambda item:item[0]))
#
# print(Data(**dict1))
#
# '''
# 匿名函数：
# lambda
# '''
# def Add(a,b):
#     print(a+b)
# Add(2,3)
#
# per = lambda a,b:a+b
# print(per(2,3))
#
# '''
# 三目运算
# '''
# a = 20
# print("True") if a >10 else print("False")
#
# '''
# 匿名函数+三目运算
# '''
# login = lambda username,password:print('登录成功') if username == 'shenqiang' and password =='123' else print('登录失败')
#
# login('shenqiang','123')
#
# '''
# 匿名函数，字典的排序
# '''
# data = lambda **kwargs:dict(sorted(kwargs.items(),key=lambda item:item[0]))
# print(data(name='shenqiang',age = 28))
#
# '''函数的内部函数map(),对列表内的同样元素做同样的事情'''
# list1 = [1,23,4,5,6]
#
# print(list(map(lambda x:x+100,list1)))
#
# '''函数的内部函数filter(),对列表内的元素进行过滤'''
# list2 = [1,2,3,4,5,6]
# print(list(filter(lambda a:a>1,list2)))

# '''
# 函数：
# 1。函数可以当作一个变量
# 2。函数是可以内部嵌套的
# 3。函数的参数也可以是函数
# '''
#
# def login(username ='shenqiang',password = '123'):
#     if username == "shenqiang" and password =="123":
#         return "1234sasa"
#     else:
#         return "False"
#
# def frofile(Token):
#     if  Token == "1234sasa":
#         print("登录成功")
#     else:
#         print("登录失败")
#
# frofile(login())
#
# '''
# 封闭：对已经实现功能的代码尽量不去修改
# 开放：对现有功能的代码进行拓展
# 需求：在调用f or f1 先打印getInfo，再打印f
# '''
# def getInfo(func):
#     def info():
#         print("无涯自动化测试")
#         func()
#     return info
#
# @getInfo
# def f():
#     print("网易云平台")
#
# @getInfo
# def f1():
#     print("51CTO平台")
#
# f()
#
# '''
# 步骤：
# 1.当我们执行getInfo时候,把被装饰的f当作参数传递
# 2.getInfo函数的返回值会重新赋值
# 3.一旦结合了装饰器，调用f函数的时候，实际调用了info内部分函数，原来的f1被覆盖
# 4。被装饰的f重新赋值给装饰器的info
# '''

# def login(func):
#     def inner(Token):
#         if Token == "01293":
#             return func(Token)
#         else:
#             print("登录失败")
#     return inner
#
# @login
# def profile(Token):
#     print("登录成功")
#
# profile("01293")


# '''
# 需求：要求注册账户，注册后的账户登录系统后，显示登录的昵称
# '''
#
# def register():
#     '''注册用户'''
#     username = input("请输入注册的账号：")
#     password = input("请输入注册的用户的密码：")
#     temp = username + '|' + password
#     with open("user.md",'w') as  f:
#         f.write(temp)
#
# def login():
#     '''登录用户'''
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     with open('user.md','r') as  f:
#         temp = f.read()
#     info = temp.split("|")
#     if username == info[0] and password == info[1]:
#         return True
#     else:
#         return False
#
# def getNick(func):
#     '''如果登录成功，获取用户昵称'''
#     with open('user.md', 'r') as  f:
#         temp = f.read()
#     info = temp.split("|")
#     if func:
#         print('{0}恭喜您登录成功！'.format(info[0]))
#     else:
#         print("登录失败，请重新登录")
#
#
# if __name__ == '__main__':
#     while True:
#         count = eval(input("1.注册，2.登录,3.退出系统"))
#         if count == 1:
#             register()
#         elif count == 2:
#             getNick(login())
#         elif count == 3:
#             import  sys
#             sys.exit(1)
#         else:
#             print("输入有误，请重新输入！")
#             continue

'''
python反射：
1.根据字符串的形式到某个模块中找东西                 ==》getattr
2.根据字符串的形式到某个模块中判断东西是否存在        ==》hasattr
3.根据字符串的形式到某个模块中设置东西               ==》setattr
4.根据字符串的形式到某个模块中删除东西               ==》delattr
'''


