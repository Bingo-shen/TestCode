#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-06 09:26
# @Author : shenqiang
# @File : simplePackage.py
# @Software: PyCharm

# import time as t
#
# # 获取当前的时间戳
# print(t.time())
#
# # 获取当前的某年某月某日 某时某分某秒
# print(t.strftime("%y-%m-%d %H:%M:%S",t.localtime(t.time())))

# import  os
#
# # print(os.system('ifconfig'))
#
# # 创建文件
# # os.mkdir("log")
#
# # # 删除文件
# # os.rmdir("log")
#
# # 重命名文件
# # os.rename('log','logs')
#
# # 当前文件的目录
# print(os.path.dirname(__file__))
#
# # 文件的上级目录
# print(os.path.dirname(os.path.dirname(__file__)))
#
# '''
# python库:
# 1.标准库
# 2.第三方库
# 3.自定义库
# sys：
# 1。变量
# 2。常用的方法
# 3。sys
# '''
# #
# import sys
# #
# # # print(sys.argv)
# # # 第一种常用方式
# # if sys.argv[1] == 'sleep':
# #     print("sleep")
# # else:
# #     print('end')
#
# # print(dir(sys))
# # print(sys.platform)
# # print(sys.version)
#
# for item in sys.path:
#     print(item)
#
# import json
# '''
# 序列化和反序列化
# 序列化：把python的数据类型转化成字符串
# 反序列化：把字符串转化成python的数据类型
# '''
# dict1 = {'name':'shenqiang','age':28}
#
# # 序列化
# dict1_str = json.dumps(dict1)
#
# print(dict1_str,type(dict1_str))
#
# # 反序列化
# str_dict1 = json.loads(dict1_str)
#
# print(str_dict1,type(str_dict1))
#
# list1 = [1,23,4,56,7]
# # 序列化
# list1_str = json.dumps(list1)
# print(list1_str,type(list1_str))
#
# # 反序列化
# str_list1 = json.loads(list1_str)
# print(str_list1,type(str_list1))
#
# tuple1 = (1,2,3,4)
# # 序列化
# tuple1_str = json.dumps(tuple1)
# print(tuple1_str,type(tuple1_str))
#
# # 反序列化
# str_tuple1 = json.loads(tuple1_str)
# print(str_tuple1,type(str_tuple1))


# import json
# import requests
#
# '''向天气预报发起请求'''
# r = requests.get(url='http://www.weather.com.cn/data/sk/101190408.html')
#
# '''
# 把查询结果写入文件
# r.content
# 对文件的序列化
# '''
# json.dump(r.content.decode('utf-8'),open('city.json','w',encoding='utf-8'))
#
# file1 = json.load(open('city.json','r',encoding='utf-8'))
#
# print(file1,type(file1))
#
# city = json.loads(file1)['weatherinfo']['city']
#
# print(city,type(city))

from urllib import parse
import hashlib

'''
MD5加密：
1。对请求的参数进行ascill吗排序 ---> dict(sorted(dict1.items(),key=lambda item:item[0]))
2。对url 进行unicode编码  --->datas = parse.urlencode(req)
3。做MD5加密    --->     98d7c955f5cf9050216087372d8fd945
'''
# dict1 = {'name':'shenqiang','age':'28','address':'nanjing','like':'vice'}
#
# req = dict(sorted(dict1.items(),key=lambda item:item[0]))
#
#
# datas = parse.urlencode(req)
#
# print(datas)
#
#
# MDfive = hashlib.md5()
#
# MDfive.update(datas.encode('utf-8'))
#
# MDfive.hexdigest()
#
# print(MDfive.hexdigest(),type(MDfive.hexdigest()))


def MD5(**kwargs):
    req = dict(sorted(kwargs.items(), key=lambda item: item[0]))
    datas = parse.urlencode(req)
    MDfive = hashlib.md5()
    MDfive.update(datas.encode('utf-8'))

    return MDfive.hexdigest()


print(MD5(name = 'shenqiang',age = '28'))


