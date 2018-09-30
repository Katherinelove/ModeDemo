import os

#coding:utf-8
#author:katherinelove
#copyright:shuai

#mkdir()  创建文件夹
#os.mkdir('girls')
#os.mkdir('boys',0o777)

#makedirs()  递归创建文件夹
#os.makedirs('/home/sy/a/b/c/d')

#rmdir() 删除空目录
#os.rmdir('girls')

#removedirs 递归删除文件夹  必须都是空目录
#os.removedirs('/home/sy/a/b/c/d')

#rename() 文件或文件夹重命名
#os.rename('/home/sy/a','/home/sy/alibaba'
#os.rename('02.txt','002.txt')

#stat() 获取文件或者文件夹的信息
#result = os.stat('/home/sy/PycharmProject/Python3/10.27/01.py)
#print(result)

#system() 执行系统命令(危险函数)
#result = os.system('ls -al')  #获取隐藏文件
#print(result)

def get_mulu_list():
    mulu_list=[d for d in  os.listdir(".")]
    print(mulu_list)
def case():
    #演示稿
    #get current work director
    local_mulu=os.getcwd()
    print(local_mulu)
    #change director

    os.chdir("F:\ModeDemo\Files")
    local_mulu = os.getcwd()
    print(local_mulu)

    #返回目录列表
    lst_mulu=os.listdir("F:\ModeDemo\os")
    for mulu in lst_mulu:
        print(mulu)

def create():
    os.makedirs("kate")
    print("添加目录kate成功")

    os.removedirs("F:\ModeDemo\Files\kate")
    print("删除目录kate成功")

    #获取文件信息
    print("获取文件信息")
    message=os.stat("F:/ModeDemo/os/OsDemo.py")
    print(message)

if __name__ == "__main__":
    #case()
    #create()
    get_mulu_list()
