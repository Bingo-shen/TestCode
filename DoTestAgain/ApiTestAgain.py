#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

def getInfo(func):
	def info():
		print("11")
		func()
	return info

@getInfo
def f():
	print("网易云平台")

@getInfo
def f1():
	print("51CTO平台")

f()


