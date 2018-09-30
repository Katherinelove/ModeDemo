#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""偏函数--当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。"""

__author__ = 'katherinelove'

import sys
import functools

def test(str):
    """注释"""
    print(test.__doc__)
    #将二进制转换为十进制
    int2=functools.partial(int,base=2)
    print(int2(str))

if __name__ == '__main__':
    test("10000000")
    print(sys.path)