#!/user/bin/env python
#coding:utf-8

#Author:shenqiang
#
# def div1(a,b):
#     return a/b
#
# def ddl(a,b):
#     try:
#         div1(a,b)
#     except Exception as E:
#         print(E.args)
#
# ddl(1,0)

'''
接口测试的纬度：
1.边界值测试（一般大型公司测试）
2.参数为空
3.参数类型
4.业务测试
自动化的范畴：
安全      性能
业务纬度测试：
1.功能接口自动化测试
    关注：
    1.用户操作流程
2.接口自动化测试
    关注：
    1.JS代码不能出问题
    2.前后端交互没有问题
    3.场景化/流程/逻辑不能出问题
    4.高频的用户场景
'''

'''
执行顺序：
try(如果执行成功)，先执行try，再执行else代码，最后执行finally
try(如果执行失败)，先执行except代码，最后执行finally
'''
def TestTry(self):
    try:
        if self == '1':
            print('try')
        else:
            print('false')
    except:
        print('except')
    else:
        print('else')
    finally:
        print('finally')

TestTry("1")



