#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 20:29
# @Author  : Roger
# @File    : oop_init.py


class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('he name is :', self.name)

p = Person('娜扎')
print(p.say_hello())
