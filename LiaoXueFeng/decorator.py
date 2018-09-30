#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""比如在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。"""

__author__ = 'katherinelove'

import functools


def mian():
    """主进程"""
    #由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
    #函数对象有一个__name__属性，可以拿到函数的名字：
    f=now
    print("now()函数名："+now.__name__)
    print("f引用的函数："+f.__name__)

    print("启用修饰器之后：")
    now()
    #print(now.__name__)

def log(func):
    """1.0本质上，decorator就是一个返回函数的高阶函数。
        2.0decorator，接受一个函数作为参数，修饰传入的函数后，并返回一个函数。
        3.0注意因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
        它们的__name__已经从原来的'now'变成了'wrapper'："""

    @functools.wraps(func)    #作用：需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
    def wrapper(*args, **kw):
        """内置函数，只是作为添加，不对func函数做修改"""
        head_deco()  #前
        func(*args, **kw)    #这里执行一边func      等同于ret= func(*args, **kw)
        last_deco()  #后
        return func         #这里不能自调用函数执行 等同于return ret
    return  wrapper
def last_deco():
    print("修饰后面的内容")
def head_deco():
    print("修饰前面的内容")
#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
#原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
@log
def now():
    print("20180923")


if __name__ == '__main__':
    mian()

