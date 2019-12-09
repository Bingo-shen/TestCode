#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang



# 模拟调用百度接口返回500的情况

import requests
from unittest import mock

def request_baidu():
    resp = requests.get('http://www.baidu.com')
    return resp.status_code

# 模拟调用request_baidu，且返回值是500
request_baidu = mock.Mock(return_value=500)
print(request_baidu())
print(request_baidu.called)#打印是否被调用
print(request_baidu.call_count)#打印调用次数



