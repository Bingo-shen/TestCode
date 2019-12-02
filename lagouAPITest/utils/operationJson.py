#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import  json
from utils.public import *
from utils.operationExcel import OperationExcel

class OperationJson:
	def __init__(self):
		self.excel=OperationExcel()

	def getReadJson(self):
		with open(data_dir(fileName='requestData.json'),encoding='utf-8') as fp:
			data = json.load(fp)
			return data

	def getRequestsData(self,row):
		'''获取请求参数'''
		return json.dumps(
			self.getReadJson()[self.excel.get_request_data(row=row)])

