#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 15:47
# @Author  : Roger
# @File    : Ds_using_dict.py
# "ab"是地址（address）簿（book）的缩写
ab = {
    'Swaroop': 'swaroop@swarropch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'mtz@ruby-lang.org',
    'roger': 'rgu@grundfos.com',
}
print("roger's address is", ab['roger'])

# 删除一个键配对
del ab['Larry']

print('\n there are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('contact{} at {}'.format(name, address))
ab['peter'] = 'peter@163.com'

for name, address in ab.items():
    print(name, address)