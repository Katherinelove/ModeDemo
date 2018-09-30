#coding:utf-8
#author:katherinelove
#copyright:shuai
from  functools import reduce


def lambad_using():
    """匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数："""
    f=lambda x: x*x
    #匿名函数lambda x: x * x实际上就是：def f(x): return x * x
    print(f(5))
def cube_func():
    """
    高阶函数，返回的是一个函数
    eg在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
    当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
    这种称为“闭包（Closure）”的程序结构拥有极大的威力。
    另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了才执行。
    返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    :return:
    """
    f1,f2,f3=countV1()
    #全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
    # 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
    print(f1(),f2(),f3())
    f1, f2, f3 =countV2()
    print(f1(), f2(), f3())
def countV2():
    """返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    如果一定要引用循环变量怎么办？方法是再创建一个函数，
    用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变："""
    def f(j):      #向外套一层，用j复制循环变量i的参数
        def g():
            return j*j
        return g            #这里一定不要写成g（） 否则只是正常函数返回的是一个值
    fs=[]
    for i in  range(1,4):
        fs.append(f(i))
    return fs
def countV1():
    """高阶函数"""
    fs=[]
    for x in  range(1,4):
        def f():
            return x*x
        fs.append(f)
    return fs

def map_using():
    #map(fun,iterator)
    lst1=map(lambda x:x*x,range(1,10))
    print(list(lst1))
    lst2=map(str,range(5))
    print(list(lst2))
    #reduce  每次都是取两个值（例外）
    lst3=reduce(lambda x,y:x*10+y,[1,6,8])
    print(lst3)
    #filter
    lst4=list(filter(lambda x:x%2==1,range(1,10)))
    print(lst4)
    #sort 返回新的列表key参数设置函数
    lst5=[16,-12,38,-24,48]
    get_list1=sorted(lst5,key=abs)
    print(get_list1)
    #  倒转
    get_list2=sorted(lst5,key=abs,reverse=True)
    print(get_list2)
    #忽略大小写排序
    lst6=["and","Bule","reduc","Hello"]
    get_list3=sorted(lst6,key=str.lower)
    print(get_list3)
def get_clip():
    lst=["a","b","c","d","e"]
    #这里的切片是深层复制
    lst_head=lst[:2]
    #last index=-1
    lst_last=lst[-3:]
    print(lst)
    print(lst_head)
    print(lst_last)
def get_list():
    '''
    列表生成式
    :return:
    '''
    lst1=[x*x for x in range(1,10) ]
    lst2=[x*x for x in range(1,10) if x%2!=0]
    lst3=[m+":"+m for m in "ABC" for n in "XYZ"]

    print(lst1)
    print(lst2)
    print(lst3)
def get_generator():
    #1.最简单的就是讲list生成式的【】  改为()
    #2.是带yield关键字的函数
    #遍历不用.next   用for循环即可
    gener1= (x*x for x in range(1,10))
    print(gener1)
    for elem in gener1:
        print(elem,end=", ")
if __name__=="__main__":
    #get_list()
    #get_clip()
    #get_generator()
    #map_using()
    #cube_func()
    lambad_using()