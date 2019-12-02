#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import os
import configparser

'''拿到文件的路径'''

def base_path(filename=None):
    return os.path.join(os.path.dirname(__file__), filename)


'''函数的默认参数处理'''
def getConfigparser(Linux='linux'):
    '''实例化对象'''
    config = configparser.ConfigParser()
    '''读取文件内容'''
    config.read(base_path('config.ini'))

    ip = config.get(Linux, 'ip')
    port = config.get(Linux, 'port')
    username = config.get(Linux, 'username')
    password = config.get(Linux, 'password')
    return [ip, port, username, password]

print(getConfigparser(),type(getConfigparser()))

# '''遍历文件内容'''
# for i in range(len(getConfigparser())):
#     print(getConfigparser()[i])

