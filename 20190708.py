#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   20190708.py
@Time    :   2019/07/08 17:58:09
@Author  :   Clifford Zhang 
@Version :   1.0
@Contact :   Clifford.zhang@royaleinternational.com
@License :   (C)Copyright 2019, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import sys

'''
print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('\n\n Python路径为：', sys.path, '\n')
'''


def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


fib(1000)
