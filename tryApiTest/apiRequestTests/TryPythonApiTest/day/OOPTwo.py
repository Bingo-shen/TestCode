#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-11-07 08:41
# @Author : shenqiang
# @File : OOPTwo.py
# @Software: PyCharm

# '''
# 普通方法：
# '''
# class Function(object):
#
#     def conn(self):
#         pass
#
#     def f(self,*args,**kwargs):
#         pass
#
#     def info(self):
#         print('我是普通方法')

# '''
# 特性方法:
# 不能有形式参数
# 被调用的时候不要加（）
# '''
# class Person(object):
#
#     @property
#     def getUserID(self):
#         pass
#
# per = Person()
# per.getUserID

# '''
# 静态方法:
# 1.直接使用类名进行调用
# 2.对象也可以调用静态方法，一般不这么做
# '''
# class Person(object):
#     @staticmethod
#     def getName(self):
#         pass
#
# Person.getName()

# '''
# 类方法：直接使用类进行调用
# '''
#
# class Person():
#     @classmethod
#     def getName(cls):
#         pass

'''
属于类：
    类属性
    静态方法
    类方法
属于对象：
    实例属性
    普通方法
    特性方法
'''
'''
继承：重用已经使用的数据和行为，减少代码的边写
子类继承所有父类的实例变量和方法
'''

# # 类属性的继承
#
# class Person(object):
#
#     def Chiness(self):
#         print('我是父类')
#
# class Body(Person):
#
#     def getName(self):
#         print('我叫沈强')
#
# body = Body()
# body.getName()
# body.Chiness()
#
#
# '''实例属性的继承和继承的两种方法'''
# class Fruit(object):
#     def __init__(self,name):
#         self.name =name
#
#
# '''由于业务需求，子类继承父类的实例属性'''
# class Apple(Fruit):
#     def __init__(self,name,brand,color):
#         '''子类继承父类的两种方式'''
#         Fruit.__init__(self,name)
#         # super(Apple,self).__init__(name)
#         self.brand = brand
#         self.color = color
#
#     def info(self):
#         return('我是水果{0},我的的品牌是{1}，我是{2}色的'.format(self.name,self.brand,self.color))
#
#
# # class Banana(Fruit):
# #     def __init__(self,brand,color):
# #         self.brand = brand
# #         self.color = color
# #
# #     def info(self):
# #         print('我是{0}牌，{1}的水果'.format(self.brand,self.color))
# #
# # banana = Banana('保健','黄色')
# # banana.info()
#
# apple = Apple('banana','baiguoyuan','yellow')
# print(apple.info())
#
# '''
# 方法的继承：
# 子类为什么重写父类的方法：子类具有自己的特性
# 当子类重写了父类的方法后，对子类进行实例化后，子类调用的方法(父类子类都存在)，执行的方法是子类的方法
# '''
#
# class Friut(object):
#
#     def eat(self):
#         print('这个可以吃')
#
#
# class Apple(Friut):
#
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#
#     '''重写父类的方法'''
#     def eat(self):
#         print('当{0}变成{1}的时候才可以吃'.format(self.name,self.color))
#
# apple = Apple('苹果','红色')
# apple.eat()

# import json
# import sys
#
# class Login(object):
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#
#     def getUsername(self):
#         return self.username
#
#     def setUsername(self,username):
#         self.username = username
#
#     def getPassword(self):
#         return self.password
#
#     def setPassword(self,password):
#         self.password = password
#
#     def register(self):
#         '''
#         注册
#         '''
#         temp = self.username+'|'+self.password
#         '''改写，序列化和反序列化'''
#         json.dump(temp,open('login', 'w'))
#         print('恭喜你注册成功！')
#
#     def login(self):
#         f = str(json.load(open('login', 'r')))
#         list1 = f.split('|')
#         if list1[0] == self.username and list1[1] == self.password:
#             return True
#         else:
#             return False
#
#     def userInfo(self):
#         '''改写，序列化和反序列化'''
#         f = str(json.load(open('login', 'r')))
#         list1 = f.split('|')
#         '''验证用户等登陆是否成功'''
#         r = self.login()
#         if r:
#             print('登陆成功！用户昵称为：{0}'.format(list1[0]))
#         else:
#             print('登陆失败！请检查您的账号和密码！')
#
#     def Exit(self):
#         sys.exit('')
#         print('您已退出该系统!')
#
# r = Login('shenqiang','shen111')
# def main():
#     while True:
#         try:
#             t = int(input('1。注册；2。登陆;3。退出登陆 \n'))
#         except Exception as e:
#             print(e.args)
#         else:
#             if t == 1:
#                 r.register()
#             elif t == 2:
#                 r.userInfo()
#             elif t == 3:
#                 r.Exit()
#             else:
#                 print('输入错误，请重新输入！')
#         finally:
#             pass
#
# if __name__ == '__main__':
#     main()

# class Function(object):
#
#     def __call__(self, *args, **kwargs):
#         print('我是__call__方法，模拟静态方法')
#
# Function.__call__('')


