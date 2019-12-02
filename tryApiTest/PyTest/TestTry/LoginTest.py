#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
import json
import sys

class Login(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def setUsername(self,username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self,password):
        self.password = password

    def register(self):
        '''
        注册
        '''
        temp = self.username+'|'+self.password
        '''改写，序列化和反序列化'''
        json.dump(temp,open('login', 'w'))
        print('恭喜你注册成功！')

    def login(self):
        f = str(json.load(open('login', 'r')))
        list1 = f.split('|')
        if list1[0] == self.username and list1[1] == self.password:
            return True
        else:
            return False

    def userInfo(self):
        '''改写，序列化和反序列化'''
        f = str(json.load(open('login', 'r')))
        list1 = f.split('|')
        '''验证用户等登陆是否成功'''
        r = self.login()
        if r:
            print('登陆成功！用户昵称为：{0}'.format(list1[0]))
        else:
            print('登陆失败！请检查您的账号和密码！')

    def Exit(self):
        sys.exit('')
        print('您已退出该系统!')

r = Login('shenqiang','shen111')
def main():
    while True:
        try:
            t = int(input('1。注册；2。登陆;3。退出登陆 \n'))
        except Exception as e:
            print(e.args)
        else:
            if t == 1:
                r.register()
            elif t == 2:
                r.userInfo()
            elif t == 3:
                r.Exit()
            else:
                print('输入错误，请重新输入！')
        finally:
            pass

if __name__ == '__main__':
    main()


