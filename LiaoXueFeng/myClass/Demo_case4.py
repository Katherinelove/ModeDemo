#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。
定制类--相当于实习对应的interface

1.__str__与__repr__     两基佬同时存在  相当于tostring（）
2.__iter__  与__next__     目的是为了迭代
    如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
3.__getitem__           实现下标获取元素
    Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
    会报错: TypeError: 'Fib' object does not support indexing
    #为了实现slice功能获取【】   需要细细实习功能
    此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
    与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
    最后，还有一个__delitem__()方法，用于删除某个元素。
4.__getattr__
    正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
    AttributeError: 'Student' object has no attribute 'score'
    要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
5.__call__
    任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

#怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
"""

__author__ = 'katherinelove'

class Fib(object):
    """斐波那契类"""
    def __init__(self):
        self.a,self.b=0,1   #初始化两个计数器a，b

    def __iter__(self):
        """实现迭代功能"""
        return self             ## 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b   #计算下一个值
        if self.a>500:   #只获取500以内的斐波那契数，否则爆出迭代完异常
            raise StopIteration
        return  self.a       #返回下一个值
    def __getitem__(self, index):
        if isinstance(index,int):
            #返回某一个值
            a,b=1,1
            #循环遍历
            for x in range(index):   #获取下一个值
                a,b=b,a+b
            return a
        if isinstance(index,slice):
            #[:]  slice类属性有start stop
            start=index.start
            stop=index.stop

            if start==None:
                start=0
            if stop==None:
                stop=-1
            a,b=1,1
            L=[]

            for i in range(stop):
                if i>=start:
                    L.append(a)
                a, b = b, a + b
            return L

class Student(object):
    """Student类"""
    def __init__(self,name,sex):
        self.__name=name
        self.__sex=sex

    def __call__(self, *args, **kwargs):
         return  [x*x for x in range(1,10)]

    def __getattr__(self, attr):
        if attr=="score":   #当对象没有此属性，解译器就会调用此方法
            return 99
    @property
    def name(self):
        return  self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self,sex):
        self.__sex=sex

    def __str__(self):
        """返回字符串"""
        return "Student object:(%s,%s)"%(self.name,self.sex)
 #   __repr__=__str__         为了将实例的变量也字符格式化  实现__repr__




#为了方便
def main():
    Student_instance()
    print("=="*50)
    Fib_instance()

def Student_instance():
    kate = Student("kate", "female")
    print(Student("eyu", "male"))
    print(kate)
    print(kate.score)
    print(kate())
    print(callable(kate))
    print(callable(int))
    print(callable([1, 2, 3]))
def Fib_instance():
    fib=Fib()
    for elem in fib:
        print(elem)
    print("fib[2]=%d"%fib[2])
    print("fib[:10]={}".format(fib[:10]))
if __name__ == '__main__':
    main()