import xlrd
import  xlwt
import os
import datetime

def write():
    #1.新建一个工作薄
    wb=xlwt.Workbook()
    #2.新建表格
    ws=wb.add_sheet('sheet1')

    #3.写入内容
    #ws.write指定style实例才能生效
    #获取style实例
    mf=xlwt.XFStyle()
    #获取字体实例
    font=xlwt.Font()    #初始化字体

    font.name='微软雅黑'
    font.bold=True
    font.underline=True
    font.italic=True

    mf.num_format_str='yyyy/mm/dd'
    mf.font=font


    ws.write(0,0,'love')     #不带样式
    ws.write(0, 1,datetime.datetime.now(), mf)  #设置样式

    #设置单元格宽度:
    ws.col(0).width=3333

    #4.保存--命名
    wb.save("wxFriends.xls")

def read():
    wb=xlrd.open_workbook('F:/ModeDemo/Files/wxFriends.xls')
    lst=wb.sheets()
    print(lst)
    ws=wb.sheet_by_name('sheet1')
    #读取方法
    #ws.row_values(rowx,start_colx,end_colx)   return list
    #ws.col_values(colx,start_rowx,end_rowx)   return list
    print("读取数据：")
    print(ws.cell(0,0))
    print(ws.cell(0,1))


if __name__=="__main__":
    os.chdir("F:/ModeDemo/Files")
    print(os.getcwd())
    write()
    read()