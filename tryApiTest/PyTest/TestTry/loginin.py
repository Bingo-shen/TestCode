#!/user/bin/env python
#coding:utf-8

#Author:shenqiang
import sys
import os
'''
python的执行路径：
1。根目录
2。环境变量
3。标准库路径
4。第三方库路径
'''
# '''查看环境变量'''
# for item in sys.path:
#     print(item)
#
# '''拼接文件到某个目录'''
base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'Fs')
# # #把fs加到环境变量
sys.path.remove(base_dir)
# '''遍历环境变量'''
for item in sys.path:
    print(item)







