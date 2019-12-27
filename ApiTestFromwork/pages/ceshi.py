#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang
import pytest

def add(a, b):
	return a + b

def test_add_integer():
	assert add(2, 3) == 5

def test_add_str():
	assert add('hi', ' wuya') == 'hi wuya'

if __name__ == '__main__':
    pytest.main()




#!/usr/bin/env python
# coding=utf-8
import pytest

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5

if __name__ =="__main__":
    pytest.main()