#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang


# 猜数字:
# 生成随机整数，从1-10取出来
# 然后输入一个数字，来猜，如果大于随机数字，则打印 比目标数字大, 如果小于随机数字，则打印 比目标数字小, 猜不对,则继续游戏, 如果猜对了，则打印 猜对了并 打印猜谜次数

import random

def Test():
    i = int(random.uniform(1, 10))
    print(i)
    count = 0
    while True:
        count = count + 1
        num = int(input("请输入数字："))
        if num>i:
            print("比目标数字大")
        elif num<i:
            print("比目标数字小")
        elif num==i:
            print(count)
            break
Test()
