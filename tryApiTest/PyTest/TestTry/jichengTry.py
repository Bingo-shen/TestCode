#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

'''
继承：重用已有的数据和方法，减少代码的重复编写
子类继承父类所有的属性和方法
'''
# # 类属性的继承
# class Person(object):
#
#     address = '地球'
#
# class UsaPerson(Person):
#     pass
#
# per = UsaPerson()
# print(per.address)
#
# '''实例属性的继承和继承的两种方法'''
# class Fruit(object):
#
#     def __init__(self,name):
#         self.name =name
#
# '''由于业务需求，子类继承父类的实例属性'''
# class Apple(Fruit):
#
#     def __init__(self,name,brand,color):
#         '''子类继承父类的两种方式'''
#         # Fruit.__init__(self,name)
#         super(Apple,self).__init__(name)
#         self.brand = brand
#         self.color = color
#
#     def info(self):
#         return('我是水果{0},我的的品牌是{1}，我是{2}色的'.format(self.name,self.brand,self.color))
#
# apple = Apple('banana','baiguoyuan','yellow')
# print(apple.info())
#
#
# '''由业务需求，子类不继承父类的实例属性'''
#
# class apple(Fruit):
#
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#
#     def info(self):
#         return('我的的品牌是{0}，我是{1}色的'.format(self.brand,self.color))
#
# apple = apple('baiguoyuan','yellow')
# print(apple.info())


# '''
# 方法的继承：
# 1.子类为什么重写父类的方法：子类要有自己的特性
# 当子类重写父类的方法后，对子类进行实例化，子类调用的方法（父类/子类）都存在，执行的方法是子类的方法（从下到下）
#
# 单个类继承的原则：
# 1。子类继承了父类，但是子类没有重写父类的方法，使用的是父类的方法（从上而下）
# 2。子类继承了父类，但是子类重写了父类的方法，使用的是子类的方法，子类优先使用自己的方法（从上而下）
# '''
# class Fruit(object):
#
#     def eat(self):
#         print ('水果是可以吃的')
#
#
# class Apple(Fruit):
#     def __init__(self,color):
#         self.color = color
#     '''重写了eat方法'''
#     def eat(self):
#         print('水果的颜色是：{0}'.format(self.color))
#
# class Banana(Apple):
#     def eat(self):
#         print('myname is banana')
#
# apple = Apple('yellow')
# apple.eat()
#
# # 需要一个对象，可以给个空对象
# Banana('').eat()

#
# '''
# 多个类继承：
# 1.从左到右
# 2.同级继承，跨级会报错
# 3.优先调用自己的函数
# '''
# class Person(object):
#     def eat(self):
#         print('Person need eat')
#
# class Mother(Person):
#     def eat(self):
#         print('her is like eat fruit')
#
# class Father(Person):
#     def eat(self):
#         print('hi is like eat Vegetables')
#
# class Son(Father,Mother):
#     pass
#
# son = Son()
# son.eat()

class A:
    def show(self):
        print('A')

class B(A):
    pass

class C(A):
    def show(self):
        print('C')
class D(B,C):
    pass

d = D()
d.show()





