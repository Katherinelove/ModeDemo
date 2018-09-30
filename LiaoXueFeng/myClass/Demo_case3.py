#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
动态语言，先创建实例后面再添加属性和方法
给实例对象添加属性和方法（MethodType（方法名，对象）），其他相同类的实例不具有
想对所有实例添加方法，直接将方法设置为类的属性

__slots__=("","")   插槽--tuple中表示只能定义的属性，否则添加其他属性会报错
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
"""

__author__ = 'katherinelove'

from types import MethodType

class Robot(object):
    def __init__(self,name,birth):
        self.__name=name
        self.__birth=birth

    @property        #getter与setter函数名称必须一致，相当于去掉__attr,通过属性访问的时还说通过getter与setter
    def birth(self):
        return self.__birth
    @birth.setter    #setter    通过birth属性访问（这儿是不能访问私有属性的，python做了处理），代码简短
    def birth(self,birth):
        self.__birth=birth

    @property                 #只读
    def age(self):
        return 2018-self.__birth
class Role(object):
    __slots__ = ("name","sex","getName")
    pass
class Sword(Role):
    __slots__ = ("score","rank")
    pass

def getName(self):
    """类中方法第一个参数必须是self"""
    return self.name
def fight(self):
    """类中方法第一个参数必须是self"""
    print("攻击成功！")


def mian():
    add_attrs_method()
    slots_application()
    getter_and_setter()
def getter_and_setter():
    """如何让getter（），setter函数变成简短属性访问"""
    #@property广泛应用在类的定义中，可以让调用者写出简短的代码
    # 同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
    robot1=Robot("kawayi",2012)
    print(robot1.age)
    robot1.birth=2010
    print(robot1.age)

def slots_application():
    role2 = Role()
    role2.name = "kate"
    role2.sex = "female"
    #role2.score = 99
    #print(role2.name + "-" + role2.sex + "-" + role2.score)
    sword1=Sword()
    sword1.name="eyu"
    sword1.sex="male"
    sword1.score=99
    sword1.rank=1
    print(sword1.name+"-"+str(sword1.rank))
def add_attrs_method():
    # 为单个实例赋予属性
    role1 = Role()
    role1.name = "曾帅"
    role1.sex = "male"
    print(role1.name + ":" + role1.sex)
    # 为单个实例赋予方法
    role1.getName = MethodType(getName, role1)
    print(role1.getName())
    # 为所有类的实例赋予相同方法
    Role.fight = fight  # 不带（）只是将函数地址赋予给类的属性
    role1.fight()
    # role2=Role()
    # print(role2.name)    #其他实例不具有此方法


if __name__ == '__main__':
    mian()

