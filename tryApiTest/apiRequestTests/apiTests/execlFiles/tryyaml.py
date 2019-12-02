#!/use/bin/env python
#coding:utf-8
#Author:shenqiang

import  csv
import  requests

'''通过接口测试的技术获取拉钩网平台的资料'''
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

def getHeaders():
	headers={
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
		'Cookie':'_ga=GA1.2.1237290736.1534169036; user_trace_token=20180813220356-b7e42516-9f01-11e8-bb78-525400f775ce; LGUID=20180813220356-b7e428ad-9f01-11e8-bb78-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEFB3FA180CE47D5CD2C77E64B1B975127F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539433248,1539529521,1539785285,1540794503; _gid=GA1.2.675811712.1540794503; _gat=1; LGSID=20181029142824-d6b66331-db43-11e8-83f6-5254005c3644; PRE_UTM=; PRE_HOST=www.bing.com; PRE_SITE=https%3A%2F%2Fwww.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; SEARCH_ID=5e964af2d19e41f1903c1f4f5b41e1a5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540794522; LGRID=20181029142843-e1d2a63c-db43-11e8-83f6-5254005c3644',
		'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95'
	}
	return headers

def laGou(page=2):
	positions=[]
	r=requests.post(
		url=url,
		headers=getHeaders(),
		data={'first':False,'pn':page,'kd':'自动化测试工程师'},
		timeout=10)
	for i in range(1,15):
		city=r.json()['content']['positionResult']['result'][i]['city']
		#区
		district=r.json()['content']['positionResult']['result'][i]['district']
		#教育
		education=r.json()['content']['positionResult']['result'][i]['education']
		#工作年限
		workYear=r.json()['content']['positionResult']['result'][i]['workYear']
		#薪资
		salary=r.json()['content']['positionResult']['result'][i]['salary']
		#公司名称
		companyFullName=r.json()['content']['positionResult']['result'][i]['companyFullName']
		#公司大小
		companySize=r.json()['content']['positionResult']['result'][i]['companySize']
		#公司标签
		companyLabelList=r.json()['content']['positionResult']['result'][i]['companyLabelList']
		#工作标签
		positionLables=r.json()['content']['positionResult']['result'][i]['positionLables']
		position={
			'城市':city,
			'区域':district,
			"学历":education,
			"工作年限":workYear,
			"薪资":salary,
			"公司名称":companyFullName,
			"公司大小":companySize,
			"公司标签":companyLabelList,
			"工作标签":positionLables
		}
		positions.append(position)
	headers=['城市','区域','学历','工作年限','薪资','公司名称','公司大小','公司标签','工作标签']
	with open('lagou.csv', 'w', encoding='gbk', newline='') as f:
		writer = csv.DictWriter(f, headers)
		writer.writeheader()
		writer.writerows(positions)
	# for item in positions:
	# 	with open('lagou.csv','w',encoding='utf-8',newline='') as f:
	# 		writer=csv.DictWriter(f,headers)
	# 		writer.writeheader()
	# 		writer.writerows(positions)
laGou()

