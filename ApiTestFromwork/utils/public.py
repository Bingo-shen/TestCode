#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import os

def data_dir(data='data',fileName=None):
    '''获取data文件的路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,fileName)




