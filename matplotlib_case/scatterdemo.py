import matplotlib.pyplot as plt

#固定格式
x_value=list(range(1,6))
y_value=[25,36,47,79,100]
plt.scatter(x_value,y_value,c="red",s=50)


#设置布局
plt.title("square",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square",fontsize=14)
plt.axis([0,6,0,100])
plt.tick_params(axis="both",labelsize=14)

plt.show()