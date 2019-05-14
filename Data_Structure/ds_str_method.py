#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 18:40
# @Author  : Roger
# @File    : ds_str_method.py

fruit1 = 'apple'
fruit2 = 'mango'
fruit3 = 'orange'
temp = ['There are ',fruit1,',',fruit2,',',fruit3,' on the table']
print(''.join(temp))
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print('_'.join(mylist))

print('there are %s, %s,%s ' % (fruit1, fruit2, fruit3))
str = fruit1+','+fruit2
print(str)