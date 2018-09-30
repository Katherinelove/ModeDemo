import itchat
import xlwt
import matplotlib.pyplot as plt
import os
import random
import math
from PIL import Image   #内置

"""
"Uin": 0,
"UserName": 用户名称，一个"@"为好友，两个"@"为群组
"NickName": 昵称
"HeadImgUrl":头像图片链接地址
"ContactFlag": 1-好友，2-群组，3-公众号
"MemberCount": 成员数量，只有在群组信息中才有效,
"MemberList": 成员列表,
"RemarkName": 备注名称
"HideInputBarFlag": 0,
"Sex": 性别，0-未设置（公众号、保密），1-男，2-女
"Signature": 公众号的功能介绍 or 好友的个性签名
"VerifyFlag": 0,
"OwnerUin": 0,
"PYInitial": 用户名拼音缩写
"PYQuanPin": 用户名拼音全拼
"RemarkPYInitial":备注拼音缩写
"RemarkPYQuanPin": 备注拼音全拼
"StarFriend": 是否为星标朋友  0-否  1-是
"Signature": 个性签名
"AppAccountFlag": 0,
"Statues": 0,
"AttrStatus": 119911,
"Province": 省
"City": 市
"Alias": 
"SnsFlag": 17
"UniFriend": 0,
"DisplayName": "",
"ChatRoomId": 0,
"KeyWord": 
"EncryChatRoomId": ""
"""
def start():
    #登录
    itchat.login()
    print("登录成功！")

    #获取好友列表【{},{}，{}，{}】
    friends=itchat.get_friends(update=True)

    foreach(friends)

    sex=get_sex(friends)
    print("man:{},femaale:{},unknow:{}".format(sex.get("man"),sex.get("women"),sex.get("unknow")))

    #Head_Img(friends)
    #createImg()
    #print("创建图像成功！")


def createImg():
    """
    遍历文件夹的图片，random.shuffle(imgs)将图片顺序打乱
    用640*640的大图来平均分每一张头像，计算出每张正方形小图的长宽，
    压缩头像，拼接图片，一行排满，换行拼接，好友头像多的话，
    可以适当增加大图的面积，
    :return:
    """
    x,y=0,0
    imgs=os.listdir("F:\ModeDemo\Files\imgs")
    #列表乱序
    random.shuffle(imgs)
    # 创建640*640的图片用于填充各小图片
    newImg = Image.new('RGBA', (640, 640))
    width=int(math.sqrt(640*640/len(imgs)))
    # 每行图片数
    line_num=(int)(640/width)
#imgs列表中只是单纯的存储名称（自带格式），但是现在被打乱了
    for index in  imgs:
        #打开一个img，缩小图片，并加入画布
        img=Image.open("F:/ModeDemo/Files/imgs/"+index)
        # 缩小图片
        img=img.resize((width,width),Image.ANTIALIAS)
        #添加到画布
        # 拼接图片，一行排满，换行拼接
        newImg.paste(img,box=(x*width,y*width))
        #x表示列，y表示行
        x+=1
        if x>=line_num:
            x=0
            y+=1
    newImg.show()
    newImg.save("all.png")


def Head_Img(friends):
    """itchat.get_head_img() 获取到头像二进制，并写入文件，保存每张头像
        itchat.get_head_img(userName="") 根据userName获取好友头像"""
    for index,friend in enumerate(friends):
        # 根据userName获取头像
        img=itchat.get_head_img(userName=friend.get("UserName"))
        #写入头像
        with open("F:/ModeDemo/Files/imgs/" + str(index) + ".jpg", "wb") as f:
            f.write(img)

def get_sex(friends):
    sex=dict()
    for friend in  friends:
        if friend["Sex"]==1: #男
            sex["man"]=sex.get("man",0)+1
        elif friend["Sex"]==2:#女
            sex["women"]=sex.get("women",0)+1
        else:
            sex["unknow"]=sex.get("unknow",0)+1
    #柱状图展示
    for  index,key in enumerate(sex):
        plt.bar(key,sex[key])
    plt.title("sex count",fontsize=24)
    plt.xlabel("sex",fontsize=14)
    plt.ylabel("count",fontsize=14)
    plt.show()
    plt.savefig("男女人数比.png")
    return sex
def calc_sex(lst):
    """方法死板，自定义方法"""
    #"Sex": 性别，0-未设置（公众号、保密），1-男，2-女
    count_male,count_female,unknow=0,0,0
    for friend in lst:
        if friend.get("Sex")==1:
            count_male=count_male+1
        elif friend.get("Sex")==2:
            count_female=count_female+1
        else:
            unknow=unknow+1
    return (count_male,count_female,unknow)

def foreach(lst):
    for item in lst:
        print(item)

if __name__=="__main__":
    start()
    #createImg()
