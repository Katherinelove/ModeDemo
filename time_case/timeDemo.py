import time
import datetime


def timeMode():
    global str_time
    # 获取当前时间--时间戳
    cur_time = time.time()
    print("当前时间:%f毫秒！" % cur_time)
    # 时间戳转时间元组struct_time
    struct_time_obj = time.localtime(time.time())
    print(struct_time_obj)
    for elem in struct_time_obj:
        print(elem, end=" ")
    print()
    # 时间元组struct_time转换为格式化字符串
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print(str_time)
    # 默认第二参数表示当前时间
    print(time.strftime("%H:%M:%S %Y-%m-%d"))
    # 将字符串解析为时间元组
    obj_struct_time = time.strptime("2017-08-06 16:30:30", "%Y-%m-%d %H:%M:%S")
    print(obj_struct_time)


def datetimeMode():
    global str_time
    # datatime模块也可以说实现
    # 获取当前时间--时间戳
    print("datatimeDemo：")
    print(datetime.datetime.now())
    # 获得日期date对象
    print(datetime.date.today())
    # 修改当前日期
    date = datetime.date(2017, 8, 18)
    print(date.day + date.month + date.year)
    # date对象格式化当前日期  datetime.date.strftime()
    str_time = date.strftime("%Y-%m-%d %H:%M:%S")
    print(str_time)
    # 转化为时间戳
    struct_time_obj=datetime.date.fromtimestamp(1537194351.202459)
    print(struct_time_obj)
    #
    # 获取时间对象
    time_ojb=datetime.time(15,30,30)
    print(time_ojb.hour,time_ojb.minute,time_ojb.second)
if __name__=="__main__":
    timeMode()
    datetimeMode()