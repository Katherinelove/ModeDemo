#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
元类
动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
type（类名，（继承），dict（定义属性，方法））
metaclass
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。

metaclass是类的模板，所以必须从`type`类型派生：
"""

__author__ = 'katherinelove'

"""
# object.__new__(cls[, ...])是一个定制方法，作用是创建类的实例，
第一个参数是类，后面的参数是用于构造实例的所有包括类名，父类和所有构造属性的参数
# 定制方法__new__()在元类定义这里使用的参数具体含义：
# cls表示元类
# name表示创建类的类名（在这里创建类就是继承Model类的子类User）
# bases表示创建类继承的所有父类
# attrs表示创建类的所有属性和方法（以键值对的字典的形式）
"""
class ListMetaclass(type):
    def __new__(cls, name, bases,attrs):
           # 方法接收到的参数依次是：
           # 当前准备创建的类的对象；
           # 类的名字；
           # 类继承的父类集合；
           # 类的方法集合。
           attrs["add"] = lambda self, value: self.append(value)
           return type.__new__(cls, name, bases, attrs)



#有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class Mylist(list,metaclass=ListMetaclass):
    pass



def fn():
    print("speak you love me！！！")

def main():
    print("动态加载类！")
    type(fn)    #可以测试类型
    Loveme=type("Loveme",(object,),dict(dump=fn))
    Loveme.dump()

def testMyList():
    print(type(Mylist))
    lst=Mylist()
    lst.add(1)
    print(lst)
if __name__ == '__main__':
    main()
    testMyList()