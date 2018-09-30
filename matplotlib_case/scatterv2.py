import matplotlib.pyplot as plt

#固定格式
x_value=list(range(1,1001))
y_value=[x*x for x in x_value]

#颜色映射  colormap  属性实例reds Blues Greens
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Greens,s=40,edgecolors="none")

#设置布局
plt.title("square",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square",fontsize=14)
plt.tick_params(axis="both",labelsize=14)

plt.show()