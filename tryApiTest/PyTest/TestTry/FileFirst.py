#!/user/bin/env python
#coding:utf-8

#Author:shenqiang

import json

'''
open的参数：
1.要操作的文件名称
2.以什么样的方式操作文件：
r：只读模式
w：只写模式【不可读，不存在就创建，存在就清空文件内容】
x：只写模式【不可读，不存在就创建，存在就报错】
a：增加模式【可读，不存在就创建，存在只增加里面的内容】
'+'表示可以同时读写某个文件，比如：
r+：读写
w+：写读
X+：写读
a+：写读
'''
file1 = open('file.json','w+')
temp = {
'name':'shenqiang',
'age':18,
'address':'nanjing'
}
# # for line in temp:
# #     file1.write(line)
# file1.writelines(temp)
# file1.close()

'''文件的序列化'''
json.dump(temp,open('file.json','w+'))

open('file.json','a')
a1 = 'haha'
file1.write(a1)
file1.close()


'''文件的上下文的处理'''
with open('Test1','w+') as T:
    T.write('这种操作方式可以系统帮助关闭，可以避免很多问题，会自动close，避免内存泄漏')