#!/user/bin/env python
#coding:utf-8

#Author:shenqiang

# # print('shenqiang')
#
# '''
# 函数的返回值：
# 1。一个函数的返回值
# 2。当一个函数没有return的关键字的时候，返回的是None
# 3。当一个函数有return的关键字的石斛，返回值是return后面的表达式或者值
#
# 函数的返回值意义：函数/方法的返回值是为了给另一个函数／方法提供一个请求参数
#
# 接口测试 查看用户信息，要查看 实现步骤：
# 1。发送post请求 login用户登陆成功
# 2。登陆成功后返回token
# 3。到这个token可以查看用户信息
# '''
#
# def login(username = 'shenqiang',password = 'shen6409175'):
#     if username == 'shenqiang' and password == 'shen6409175':
#         return 'loginsuccess'
#     else:
#         return 'login fail'
#
# def userInfo(token):
#     '''查看用户信息'''
#     if token == 'loginsuccess':
#         print('我的订单信息')
#     else:
#         print('logout')
#
# userInfo(login())
#

dict1 = {'name':'shenqiang'}

print(dir(dict1))













