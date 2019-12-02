#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

'''豆瓣网'''
import requests
params = {'search_text':'沈强','cat':'1002'}
url = requests.get(url='https://movie.douban.com',params=params)
'''网络协议状态码'''
print(url.status_code)
'''请求正文，返回内容为text格式的字符串'''
print(url.text)
# '''解码成utf-8'''
# print(url.content.decode('utf-8'))
# '''请求地址'''
# print(url.url)
# '''请求地址的编码'''
# print(url.encoding)
# '''除非确定是json格式的字符串，不然不要使用json方法'''
# # print(url.json())


'''拉勾网爬取数据'''

import requests
data = {'first':'true','pn':1,'kd':'自动化测试'}
headers = {
    'Accept':'application/json',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Cookie':'*'
   }
r =requests.post(url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',data=data,headers=headers,verify=False,timeout = 5)
print(r.text)

# a = '%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88'
# print(a.encode('utf-8'))



