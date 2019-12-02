#!/user/bin/env python
#coding:utf-8
#Author:shenqiang
#
# '''
# 普通方法
#     动态方法（万能参数）
# 特性方法
#
# '''
#
# class Person():
#
#     def cnn(self):
#         pass
#
#     def f1(self,*args,**kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#     def info(self):
#         print('这是个普通的方法')
#
# per = Person()
# per.info()

#
# '''
# 特性方法：不能有形式参数
# '''
# class person(object):
#     '''特性方法调度@property'''
#     @property
#     def getUserId(self):
#         pass
#
# per = person
# per.getUserId

'''
静态方法：直接使用类名进行调用，它属于类
对象可以直接调用静态方法，一般不建议这么做
'''
class MYSQL(object):
    '''静态方法，直接提供给全局调用'''
    @staticmethod
    def cnn(cls):
        pass

MYSQL.cnn()

'''
类方法：直接使用类来调用
'''
class Person(object):

    @classmethod
    def cnn(cls):
        pass
'''
属于类的：
    类属性
    静态方法
    类方法
属于对象的：
    实例属性
    普通方法
    特性方法
'''

