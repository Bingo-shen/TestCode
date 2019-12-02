#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang
import json

from utils.operatJson import OperatJson

operatjson = OperatJson()

def setJsonData(kd=''):
    '''对email这个动态参数进行赋值'''
    dict1 = json.loads(operatjson.getRequestsData(1))
    dict1['email'] = kd
    return dict1

def setNameLoginOrEmail(name = 'shen',loginOrEmail='shen'):
    '''对email这个动态参数进行赋值'''
    dict2 = json.loads(operatjson.getRequestsData(2))
    dict2["name"] = name
    dict2["loginOrEmail"] = loginOrEmail
    return dict2

