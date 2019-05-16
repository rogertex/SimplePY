#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 20:29
# @Author  : Roger
# @File    : oop_init.py


class Person:
    def __init__(self, name, question):
        self.roger = name
        self.question = question
    def say_hello(self):
        print('he name is :', self.roger, self.question)

p = Person('娜扎',['老板','colleague'])
print(p.say_hello())

