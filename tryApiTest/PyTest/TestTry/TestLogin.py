#!/user/bin/env python
#coding:utf-8

#Author:shenqiang
import json

'''分离用户名输入和密码输入的函数'''
def infoUsername():
    '''
    输入用户名
    :return: username  用户名
    '''
    username = input('请输入您注册的用户名：\n')
    return username

def infoPassword():
    '''
    输入密码
    :return:password 密码
    '''
    password = input('请输入您注册的密码：\n')
    return password

'''
注册
'''
def register(username,password):
    '''
    注册
    :parameter: username 用户名
    :parameter:password 密码
    :return:
    '''
    temp = username+'|'+password
    '''改写，序列化和反序列化'''
    json.dump(temp,open('login', 'w'))
    # f = open('login','w')
    # f.write(temp)
    print('恭喜{0},注册成功！'.format(username))

'''
1。模拟登陆
2。模拟登陆成功后，用户现实登陆状态
3。模拟注册
'''
def login(username,password):
    '''
    登陆
    :param username:登陆系统的账号
    :param password:登陆系统的账号的密码
    :return: True：登陆成功 False：登陆失败
    '''
    # f = open('login','r')

    '''改写，序列化和反序列化'''
    f = str(json.load(open('login','r')))
    list1 = f.split('|')
    if list1[0] == username and list1[1] == password:
        return True
    else:
        return False

    # for line in f:
    #     # 将字符串转化成列表
    #     list = line.split('|')
    #     if list[0] == username and list[1] == password:
    #         return True
    #     else:
    #         return False


'''
查询用户信息
'''
def info(username,password):
    '''拿到文件的用户名和密码'''

    # lines = open('login','r')
    # for line in lines:
    #     list1 = line.split('|')

    '''改写，序列化和反序列化'''
    f = str(json.load(open('login', 'r')))
    list1 = f.split('|')
    '''验证用户等登陆是否成功'''
    r = login(username,password)
    if r:
        print('登陆成功！用户昵称为：{0}'.format(list1[0]))
    else:
        print('登陆失败！请检查您的账号和密码！')

'''
退出系统
'''
def exit():
    '''退出系统'''
    import sys
    sys.exit(1)
    print('您已退出该系统!')

'''
主函数
'''
def main():
    '''调用上面的方法和属性'''
    while True:
        try:
            # t = int(input('1。注册；2。登陆;3。退出登陆 \n'))
            t = int(input('1。注册；2。登陆;3。退出登陆 \n'))
        except Exception as e:
            print(e.args)
        else:
            if t == 1:
                username = infoUsername()
                password = infoPassword()
                register(username,password)
            elif t == 2:
                username = infoUsername()
                password = infoPassword()
                login(username,password)
                info(username,password)
            elif t == 3:
                exit()
            else:
                print('输入错误，请重新输入！')
        finally:
            print('')

if __name__ == '__main__':
    main()







