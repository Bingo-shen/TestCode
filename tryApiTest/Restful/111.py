#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import random
i = 1
while True:
    aim_num= random.randint(1, 10)
    num = int(input("请输入一个数字："))
    guess = input("猜测比目标数字（大，小，相等）：")
    print("*" * 20)
    print("数字：%s" % num)
    print("猜测大小：%s" % guess)
    print("目标数字数字：%s" % aim_num)
    print('*' * 20)

    if num > aim_num:
        if guess =='大':
            print("比目标数字大,猜测：第%s次猜中" % i)
            print("=" * 20)
            break
        elif guess == '小':
            print("猜错了，别灰心，再来")
            print("=" * 20)
            i += 1
        elif guess == '相等':
            print("猜错了，别灰心，再来")
            print("=" * 20)
            i += 1
    elif num < aim_num:
        if guess == '小':
            print("比目标数小,猜测：第%s次猜中" % i)
            print("=" * 20)
            break
        elif guess =='大':
            print("猜错了，别灰心，再来")
            print("=" * 20)
            i += 1
        elif guess == '相等':
            print("猜错了，别灰心，再来")
            print("=" * 20)
            i += 1
    elif num == aim_num:
        if guess == '相等':
            print("等于目标数,猜测：第%s次猜中" % i)
            print("=" * 20)
            break
        elif guess =='大':
            print("猜错了，别灰心，再来")
            print("=" * 20)
            i += 1
        elif guess == '小':
            print("猜错了，别灰心，再来")
            print("=" * 20)
            i += 1

    else:
        print("请输入正确数字！！！")
