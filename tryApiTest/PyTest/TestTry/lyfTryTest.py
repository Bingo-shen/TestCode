#!/user/bin/env python
#coding:utf-8

#Author:shenqiang
import json
import requests

# '''请求来伊份后台地址'''
# base_url = requests.post(url='',data={},deaders ={})
#
# '''输出网络状态码'''
# print(base_url.status_code)
#
# '''输出返回的参数'''
# print(base_url.text,type(base_url.text))
#
# '''如果输出的text是str格式的文件,需要序列化和反序列化'''
# r = json.loads(base_url.text)
# print(r,type(r))

'''向天气预报发起请求'''
r = requests.get(url='http://www.weather.com.cn/data/sk/101190408.html')

# '''把编码成utf-8'''
# print(r.content.decode('utf-8'))

'''对文件进行序列化-->把服务的响应写入某个文件中'''
json.dump(r.content.decode('utf-8'),open('login.json','w',encoding='utf-8'))

'''对文件进行反序列化，获取读取文件的内容'''
load = json.load(open('login.json','r'))

print(load,type(load))

'''对str类型文件内容进行反序列化，读取city的value'''
city = json.loads(load)['weatherinfo']['city']

print('查询的城市是：',city)

