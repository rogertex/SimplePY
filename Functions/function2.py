#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 23:00
# @Author  : Roger
# @File    : function2.py


def max_parm(a, b):
    if a > b:
        print(a, ' is maximum')
    elif a == b:
        print(a, 'equals', b)
    else:
        print(b, ' is maximum')


max_parm(3, 4)
x = 5
y = 7
max_parm(x, y)