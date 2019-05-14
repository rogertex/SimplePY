#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 10:13
# @Author  : Roger
# @File    : global_variables.py

x=40

def func():
    global x
    print('first variable', x)
    x = 50
    print('global', x)


func()
