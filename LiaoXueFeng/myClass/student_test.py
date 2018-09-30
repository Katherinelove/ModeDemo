#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Student类运用"""

__author__ = 'katherinelove'
from LiaoXueFeng.myClass.student import Student
import types


def access():
    eyu=Student("eyu","male",97,2)
    yuren=Student("yuren","female",99,1)
    print(eyu.__class__)
    print(Student.__name__)
    print(Student.__qualname__)
    print(eyu.__dict__)
    print(eyu.__class__.__qualname__)
    print("="*50)
    print("({},{},{},{})".format(eyu.getName(),eyu.getSex(),eyu.getScore(),eyu.getRank()))
    print("=" * 50)
    print(isinstance(eyu,Student))
    #但是type()函数返回的是什么类型呢？它返回对应的Class类型。
    print(type(eyu))
    #如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
    print(type(fn))
    print(type(fn)==types.FunctionType)
    print(type(abs)==types.BuiltinFunctionType)
    print( type(lambda x: x)==types.LambdaType)
    print(type((x for x in range(10)))==types.GeneratorType)
    #并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
    print(isinstance([1, 2, 3], (list, tuple)))
    print(isinstance((1, 2, 3), (list, tuple)))
    #####总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

def get_all_attr():
    """如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
    比如，获得一个str对象的所有属性和方法："""
    #类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
    #如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
    # 它自动去调用该对象的__len__()方法，
    # 所以，下面的代码是等价的：
    print("="*50)
    print(len('ABC'))
    print("ABC".__len__())
    print("=" * 50)
    lst1=dir("adc")
    print(lst1)
    goutou=Student("goutou","male",88,3)
    #探索对象拥有的属性，方法
    #仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
    print(hasattr(goutou,"_Student__name"))
    print(hasattr(goutou,"name"))

    print(getattr(goutou,"_Student__name"))     #goutou对象有name属性（私有属性）吗,有就返回
    print(getattr(goutou,"name","404"))         #goutou对象有name属性（私有属性）吗,没有就返回默认值404
    #如果试图获取不存在的属性，会抛出AttributeError的错误：
    #getattr(goutou,"123")

    setattr(goutou,"English",100)
    print(hasattr(goutou,"English"))
    print(getattr(goutou,"English","没有English属性"))
    print("=" * 50)
    #通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
    # 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
    #直接就可以通过实例属性访问，就不要用 setattr()， getattr()
    """
    一个正确的用法的例子如下：
    def readImage(fp):
        if hasattr(fp, 'read'):
            return readData(fp)
        return None
    假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
    如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
    
    请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，
    也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
    """
def fn():
    pass
if __name__ == '__main__':
    #access()
    get_all_attr()