#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 14:57
# @Author  : Roger
# @File    : Ds_using_list.py
# This is my shopping list
shopplist = ['apple', 'mango', 'carrot', 'banana']
print('i have', len(shopplist), 'items to purchase')

print('these items are:', end=' ')
for item in shopplist:
    print(item,end=' ')
print('\n i also have to buy rice')
shopplist.append('rice')
print('my shopping list is now',shopplist)

print('i will sort my shopping list')
shopplist.sort()
print('the sorted list is:',shopplist)

print('The first item i will buy is',shopplist[0])
olditem = shopplist[0]
del shopplist[0]
print('i bought the ', olditem)
print('my shopping list is now:', shopplist)
