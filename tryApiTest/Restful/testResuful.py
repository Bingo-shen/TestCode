# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Author : shenqiang
# # '''
# # 递归的简单实现,输出i = 5的时候的结果
# # '''
# # def diGui(i=0):
# #     i = i + 1
# #     return ("{0}大于等于5".format(i)) if i>=5 else diGui(i)
# # print(diGui())
#
#
# dict1 = {'first':False,"pn":1,"kd":"自动化测试"}
#
# def sendParam(pn=None,kd=None):
#     data = dict1
#     data["pn"] = pn
#     data["kd"] = kd
#     return data
#
# def test_001():
#     '''测试pn为空'''
#     sendParam(kd="自动化测试")
#
# def test_002():
#     '''测试kd为空'''
#     sendParam(pn=2)
#
# def test_003():
#     '''测试pn、kd都为空'''
#     sendParam()
#
# def test_004():
#     '''测试pn的数据类型为字符型'''
#     sendParam(pn="2")
# #

# a = [1,2,[3,4]]
# b = a[-1]
# b.append(4)
# print(a)

# def f(*args,**kwargs):
#     return args,kwargs
# result = f((1,2,3),a=2)
# print(result)

