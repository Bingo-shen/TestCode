#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import json

'''
序列化：把python的数据类型转化成str的类型的过程
反序列化：反序列化就是把str的数据类型转化成python的数据类型结构
'''

'''字典的序列化和反序列化'''
dict_str = {'name':'shenqiang','age':18,'address':'shanghai'}

#序列化，字典转化成字符串
str_dict = json.dumps(dict_str)

print(str_dict,type(str_dict))

#反序列化，字符串转化成字典
dict_str = json.loads(str_dict)

print(dict_str,type(dict_str))


'''列表的序列化和反序列化'''
list_str = ['shenqiang','18','nanjing']

#列表序列化
str_list = json.dumps(list_str)

print(str_list,type(str_list))

#列表反序列化
list_str = json.loads(str_list)

print(list_str,type(list_str))


'''元祖的序列化和反序列化'''
tuple_str = ('shenqiang','20','nanjing')

#元祖的序列化
str_tuple = json.dumps(tuple_str)

print(str_tuple,type(str_tuple))

#元祖的反序列化
tuple_str = json.loads(str_tuple)

print(tuple_str,type(tuple_str))


