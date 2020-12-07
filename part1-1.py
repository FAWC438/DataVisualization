import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率
plt.style.use('bmh')

fig, ax = plt.subplots()
ax.set_title("立方值函数图像")
x_list = [i for i in range(-10, 11)]
x = np.array(x_list)  # 创建一个numpy数组x
y = x ** 3  # 创建一个numpy数组y，内容为x中数据的立方值
plt.bar(x, y, color='y')  # bar的颜色改为红色
for a, b in zip(x, y):  # 在直方图上显示数字
    if a % 2 == 0:
        plt.text(a, -60, '%d' % a, ha='center', va='bottom', fontsize=8)
    plt.text(a, b / 2, '%d' % b, ha='center', va='bottom', fontsize=8, color='blue')
plt.xlabel('-10至10之间的整数')
plt.ylabel('立方值')
plt.tight_layout()
plt.savefig('part1-1.png')
plt.show()
