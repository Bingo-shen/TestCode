#!/use/bin/env python
#coding:utf-8

#Author:WuYa

import  unittest
import  os
import  smtplib
from email.mime.text import MIMEText

from utils.operationExcel import OperationExcel

class Runner:
	def __init__(self):
		self.excel=OperationExcel()

	def getSuite(self):
		'''获取要执行的测试套件'''
		suite = unittest.TestLoader().discover(
			start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests'),
			pattern='test_*.py',
			top_level_dir=None)
		return suite

	def send_mail(self,to_user,sub,content):
		'''
		发送邮件内容
		:param to_user:发送邮件的人
		:param sub:主题
		:param content:邮件内容
		'''
		global  send_mail
		global  send_user
		send_mail = 'smtp.sina.cn'
		send_user='wuya1303@sina.com'
		message=MIMEText(content,_subtype='plain',_charset='utf-8')
		message['Subject']=sub
		message['From']=send_user
		message['To']=to_user
		server=smtplib.SMTP()
		server.connect(send_mail)
		server.login('wuya1303@sina.com','admin123')
		server.sendmail(send_user,to_user,message.as_string())
		server.close()

	def main_run(self):
		'''批量执行测试用例'''
		unittest.TextTestRunner().run(self.getSuite())
		content='通过数：{0} 失败数：{1} 通过率：{2}'.format(
			self.excel.run_success_result(),
			self.excel.run_fail_result(),self.excel.run_pass_rate())
		print('Please wait while the statistics test results are sent in the mail')
		self.send_mail('2839168630@qq.com','接口自动化测试报告',content)

if __name__ == '__main__':
	Runner().main_run()
