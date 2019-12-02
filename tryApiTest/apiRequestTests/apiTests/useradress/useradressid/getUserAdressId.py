#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-09-02 11:32
# @Author : shenqiang
# @Site : 
# @File : getUserAdressId.py
# @Software: PyCharm

import requests
from lxml import etree

# 获取源码
html = requests.get("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html")
# print(html.text)
# # 打印源码
# etree_html = etree.HTML(html.text)
# pathUrl = "/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody"
# content = etree_html.xpath("/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[4]/td[1]/atext()")
# content1 = pathUrl+'/tr[4]/td[1]/a/text()'
#
# print(content1)
# print(content)
# for each in content:
#     print(each)













