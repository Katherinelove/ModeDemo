import matplotlib.pyplot as plt

#固定格式
x_value=list(range(1,6))
y_value=[x*2 for x in x_value]

plt.plot(x_value,y_value,linewidth=5,c=(0,1,0))

#设置布局
plt.title("square",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square",fontsize=14)

plt.tick_params(axis="both",labelsize=14)

plt.show()