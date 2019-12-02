#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-25 19:47
# @Author : shenqiang
# @File : requestsAnalysis.py
# @Software: PyCharm

# import json
# import requests
#
# # r = requests.get("https://www.douban.com")
# # print(r.json())
# # print(r.text)
# # print(r.status_code)
# # print(r.content.decode("utf-8"))
#
# requests.post()

import json
import requests

headers = {'Content-Type':'application/json;charset=UTF-8','Referer':'http://lyfadmin.edu.laiyifen.com/plugins/platform-include/views/login.html'}

'''注意区分post方法里面什么时候使用data，什么时候使用json'''
data={"username":"lyfadmin","password":"liuhaijun123456","type":1}

r = requests.post(url='http://lyfadmin.edu.laiyifen.com/ouser-web/mobileLogin/login.do',
                  json=data,
                  headers=headers
                  )
'''公司后台返回的是字符串'''
# print(r.text,type(r.text))
'''
1。调用indent进行格式转换，转换成json格式
2。调用ensure_ascii进行编码转换，unicode编码的汉语转换成utf-8的汉语
'''
print(json.dumps(r.json(),indent=True,ensure_ascii=False),type(r.json()))







