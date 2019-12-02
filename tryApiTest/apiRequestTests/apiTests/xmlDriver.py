#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import  xml.dom.minidom
import  os

def getXml(value=None):
	'''获取单节点的数据内容'''
	xmlFile=xml.dom.minidom.parse('data.xml')
	db=xmlFile.documentElement
	itemList=db.getElementsByTagName(value)
	item=itemList[0]
	return item.firstChild.data


def getUser(parent='WuYA',child=None):
	'''获取单节点的数据内容'''
	xmlFile=xml.dom.minidom.parse('data.xml')
	db=xmlFile.documentElement
	itemList=db.getElementsByTagName(parent)
	item=itemList[0]
	return item.getAttribute(child)

print(getUser(child='address'))


