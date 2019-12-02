#!/user/bin/env python
#coding:utf-8

#Author:shenqiang

'''
类：是由一些属性和方法组成的
'''
# def f():
#     pass

''' 
f2 = f()
f1 = f()
print(id(f1))
print(id(f2))

python3的一个对象，映射关系是同一个id。python2的对象，每次调用都会新生成一个地址
对象的创建--->类的事例化过程
三个特性：
1.对象的句柄--->区分不同的对象
2.属性
    共有属性
        类属性（共同的属性分离出来）：属于类也属于对象
        实例属性：只属于对象
        局部变量
    私有属性
3.方法  
'''
# class Person(object):
#     '''类型属性'''
#     gongtong = 'China'
#     def __init__(self,name,age):
#         '''实例属性'''
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#     def setName(self,name):
#         self.name = name
#
#     def setAge(self,age):
#         self.age = age
#
#     def info(self):
#         return 'name:{0},age:{1},address:{2}'.format(self.name,self.age,self.gongtong)
#
# # 实例化Person
# pel = Person('沈强',18)
# print(pel.getAge(),pel.getName())
# print(pel.info())

'''
满足所有人类的个性，调用万能参数
构造函数：即使没写构造函数，类都是有构造函数的
一个类可以有多个构造函数，建议一个类只有一个构造函数
构造函数用来：
1.初始化属性
# '''
# class Persons(object):
#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#     def info(self):
#         print(self.kwargs.values())
#
# per = Persons(name='shenqiang')
# per.info()
#
# per1 = Persons(name='shenqiang',age = 18,address = 'nanjing')
# per1.info()

'''析构函数的执行顺序：
对象实例化->构造函数->对象调用方法->代码跳转到具体的方法->执行方法的代码块->最后执行析构函数
'''
class person(object):
    def __init__(self):
        print('我是构造函数')

    def __del__(self):
        print('我是析构函数')

    def info(self):
        print('我是方法')

per = person()
per.info()






# for i in range(10):
#     print(i)
#
# import requests
#
# r = requests.post(url='http://www.baidu.com')
# print(r.status_code)
# print(r.text)


