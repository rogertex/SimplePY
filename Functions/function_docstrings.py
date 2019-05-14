#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 14:56
# @Author  : Roger
# @File    : function_docstrings.py


def print_max(x, y):
    ''' Please print the max value.

    this document is only for explaining some important
    things to easy understand this function. '''
    x = int(x)
    y = int(y)
    if x > y :
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print_max(3, 5)
print(print_max.__doc__)


