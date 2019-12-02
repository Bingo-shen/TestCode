#!/user/bin/env python
#coding:utf-8

#Author:shenqiang

import time as t

'''获得时间戳'''
print(int(t.time()))

'''获得年月日'''
print(t.localtime(t.time()))

'''获得易读的年月日'''
print(t.strftime('%y-%m-%d %H:%M:%S',t.localtime()))



