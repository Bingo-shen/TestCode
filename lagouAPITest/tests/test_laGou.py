#!/use/bin/env python
#coding:utf-8 

#Author:WuYa

import  unittest
import  json
from base.method import Method,IsContent
from page.laGou import *
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

class LaGou(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.p=IsContent()
		self.execl=OperationExcel()
		self.operationJson=OperationJson()

	def statusCode(self,r):
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['code'], 0)

	def isContent(self,r,row):
		self.statusCode(r=r)
		self.assertTrue(self.p.isContent(row=row,str2=r.text))

	def test_laGou_001(self):
		'''拉钩:测试翻页'''
		r = self.obj.post(row=1,data=self.operationJson.getRequestsData(1))
		self.isContent(r=r,row=1)
		self.execl.writeResult(1,'pass')

	def test_laGou_002(self):
		'''拉钩:测试关键字的职位搜索'''
		r =self.obj.post(row=1,data=setSo('Python开发工程师'))
		list1=[]
		for i in range(0,15):
			positionId=r.json()['content']['positionResult']['result'][i]['positionId']
			list1.append(positionId)
		writePositionId(json.dumps(list1))

	def test_lgGou_003(self):
		'''访问搜索到的每个职位的详情页信息'''
		for i in range(15):
			r=self.obj.get(url=getUrl()[i])
			self.assertTrue(self.p.isContent(34,r.text))

if __name__ == '__main__':
    unittest.main(verbosity=2)
