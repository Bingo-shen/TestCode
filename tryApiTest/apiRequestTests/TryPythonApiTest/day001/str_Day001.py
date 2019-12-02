#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-04 08:13
# @Author : shenqiang
# @File : str_Day001.py
# @Software: PyCharm

'''
基本练习
'''
# # 输出方法
# name = input("what's your name:")
# # help(type(name))
# print(dir(name))

# # 三个上引号可以进行多行输出
# print("""
# 你好
# 谢谢
# """)
#
# import requests
# print(dir(requests))

'''
循环、判断和筛选
'''
# age = 25
# if age > 20:
#     print("True")
# elif age > 25:
#     print("正确的")
# else:
#     print("False")
#
# a = True
# if a:
#     print("正确")
# else:
#     print("错误")

# for i in range(0,10):
#     print(i)
#
# while True:
#     p = input("1.年龄 2.名字")
#     if p == "1":
#         age = input("你的年龄是：\n")
#         print("你的年龄是"+age+"岁")
#         break
#     elif p == "2":
#         name = input("你的名字是：\n")
#         print("你的名字叫"+name)
#         break
#     else:
#         print("""
#         您的输入有误，请重新输入！
#         有效数字区间在【1，2】
#         其中：1.年龄 2.名字
#         """)

'''
字符串的相关方法
'''
# str1 = "1"
# str2 = str1.replace("1","admin")
# print(str2)
# print(str2.startswith("a"))
# print(str2.endswith("m"))
# print(str2.isdigit())

# str1 = "你好，沈强"
# list1 = str1.split('，')
# print(list1)
# str2 = "，".join(list1)
# print(str2)
# print(dir(str2))
# print(type(str2))

# name = "沈强"
# age = 28
# print("我的名字叫{0},我的年龄{1}".format(name,age))
# print("我的名字叫%s，我的年龄%d"%(name,age))
# print("我的名字叫{name}，我今年{age}岁".format(name=name,age=age))

'''
列表的相关方法和列表推导式
'''
# list1 = [1,2,3,4,5,2,3,0,8]
# list2 = [3,3,3]
# # print(dir(list1))
# list1.append(99)
# print(list1)
# list1.insert(0,22)
# print(list1)
# count1 = list1.count(2)
# print(count1)
# print(list1.index(4))
# list1.remove(0)
# print(list1)
# list1.pop()
# print(list1)
# list1.extend(list2)
# print(list1)
# list1.reverse()
# print(list1)
# list1.sort()
# print(list1)
# for i in  list1:
#     if i >= 3:
#         print(i)
# print([x+1 for x in list1])
# print([x+1 for x in list1 if x>3])

'''
字典的方法
'''
# tuple1 = (1,23,4,["shenqiang","28"],{"name":"shenqiang","age":"28"})
# tuple1[3][1] = "29"
# print(tuple1)
# tuple1[4]["name"] = "沈强"
# print(tuple1)
# print(dir(tuple1))
# dict1 = {'name':'shenqiang','age':'28'}
# dict2 = {'adress':'nanjing'}
# dict1.update(dict2)
# print(dict1)
# dict3 = dict1
# print(dict3)
# print(sorted(dict3.items(),key=lambda item:item[0]))
# print(dir(dict1))
# # dict1.clear()
# # print(dict1)
# dict1['name'] = '沈强'
# print(dict1)
# print(dict1.get('age'))
#
# for key in dict1.keys():
#     print(key)
#
# for key,value in  dict1.items():
#     print(key,value)

