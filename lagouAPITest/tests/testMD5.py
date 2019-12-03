#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

# 针对平台加密数据处理啊
'''
接口自动化需求和问题：
“1.对请求参数按照key-value的格式，进行参数名的ascill码排序
- 请求参数不确定
- 怎么排序
2.在第一步的结果字符串尾部拼接密钥
- name=shenqiang&age=28&address=nanjing&sex=boy+密钥
3.排序后，对请求的参数进行MD5加密“
- hashlib

解决方法（核心：解决问题的思路）
1.请求参数不确定--->动态参数 *args，**kwargs
2.怎么排序--->			sorted()
3.请求地址尾部密钥拼接可以用urllib的parse
4.hashlib加密
'''

from urllib import parse
import hashlib

def dataSign(secure='shenqiang',*args,**kwargs):
    '''对字典的key进行排序'''
    dict2 = dict(sorted(kwargs.items(),key=lambda item:item[0]))
    '''对url进行拼接'''
    str1 = parse.urlencode(dict2)+secure
    '''进行MD5加密'''
    # 实例化MD5
    md = hashlib.md5()
    md.update(str1.encode('utf-8'))
    return md.hexdigest()

'''data2参数不确定'''
data2 = {"a":"2","c":"1","b":"3"}

print(dataSign(**data2))


