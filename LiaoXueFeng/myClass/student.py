#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""note"""

__author__ = 'katherinelove'

class Student(object):
    """
    学生类
    """
    def __init__(self ,name,sex,score,rank):
        self.__name=name
        self.__sex=sex
        self.__score=score
        self._rank=rank
        
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    def getSex(self):
        return  self.__sex
    def setSex(self,sex):
        self.__sex=sex
    def getScore(self):
        return self.__score
    def setScore(self,score):
        self.__score=score
    def getRank(self):
        return self._rank
    def setRank(self,rank):
        self._rank=rank
