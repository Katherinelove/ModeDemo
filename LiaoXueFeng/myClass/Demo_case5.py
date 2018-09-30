#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""枚举类的使用"""

__author__ = 'katherinelove'

from enum import Enum,unique
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

@unique           #保证唯一性
class weekDay(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sta=6


def main():
    #直接获取enum类
    #遍历
    for name,meber in weekDay.__members__.items():
        print(name,meber,str(meber.value))
    print(weekDay.Fri)
    print(weekDay.Sun==weekDay.Sta)
if __name__ == '__main__':
    main()