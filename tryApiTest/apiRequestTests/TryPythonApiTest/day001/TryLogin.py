# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 2019-11-04 22:10
# # @Author : shenqiang
# # @File : TryLogin.py
# # @Software: PyCharm

import  json

'''
需求：要求注册账户，注册后的账户登录系统后，显示登录的昵称
'''
def inUserName():
    '''
    :param username:用户名
    :return username:用户名
    '''
    username = input("请输入用户名：")
    return username

def inPassWord():
    '''
    :param password:密码
    :return password:密码
    '''
    password = input("请输入密码：")
    return password

def register():
    '''注册用户'''
    username,password = inUserName(),inPassWord()
    temp = username + '|' + password
    json.dump(temp,open('user.md','w'))

def login():
    '''登录用户'''
    username, password = inUserName(),inPassWord()
    temp = json.load(open('user.md','r'))
    info = temp.split("|")
    if username == info[0] and password == info[1]:
        return True
    else:
        return False

def getNick(func):
    '''如果登录成功，获取用户昵称'''
    temp = json.load(open('user.md', 'r'))
    info = temp.split("|")
    if func:
        print('{0}恭喜您登录成功！'.format(info[0]))
    else:
        print("登录失败，请重新登录")

if __name__ == '__main__':
    while True:
        try:
            count = eval(input("1.注册，2.登录, 3.退出系统"))
            if isinstance(count,float):
                count = int(count)
        except Exception as  e:
            print(e.args)
        else:
            if count == 1:
                register()
            elif count == 2:
                getNick(login())
            elif count == 3:
                import sys
                sys.exit(1)
            else:
                print("输入有误，请重新输入！")
                continue


'''sorted()方法小练习'''
dict1 = {'name':'shenqiang','age':'28','address':'nanjing'}
print(dict(sorted(dict1.items(),key=lambda item:item[0])))



