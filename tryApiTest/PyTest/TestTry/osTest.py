#!/user/bin/env python
#coding:utf-8

#Author:shenqiang
import os

'''调用计算机系统的指令'''
print(os.system('ifconfig'))

'''创建文件夹'''
os.mkdir('/Users/apple/Desktop/log')

# '''删除文件夹'''
# os.rmdir('/Users/apple/Desktop/log')

'''文件重命名'''
os.rename('/Users/apple/Desktop/log','/Users/apple/Desktop/Newlog')

'''当前文件所在路径'''
print('当前目录在哪个路径下',os.path.dirname(__file__))

'''当前文件所在路径的上一级路径'''
print('当前文件所在路径的上一级路径',os.path.dirname(os.path.dirname(__file__)))

'''当前文件所在路径的上一级路径的上一级路径'''
print('当前文件所在路径的上一级路径的上一级路径',os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

'''当前文件的全路径'''
print(__file__)

'''拿到文件的上级目录'''
base_dir = os.path.dirname(os.path.dirname(__file__))

'''拼接login文件里面的内容'''
file1 = open(os.path.join(base_dir,'login'),'r')

'''输出读取的文件内容'''
print(file1.read())

'''关闭文件'''
file1.close()

'''当一个接口的参数个数未知'''
def f(*args,**kwargs):
    return kwargs

'''返回的是一个字典'''
print(f(age='18',address='nanjing'))

print(f(name='shenqiang',age='18',address='nanjing'))



