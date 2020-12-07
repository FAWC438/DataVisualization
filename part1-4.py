import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率

fig, ax = plt.subplots()
x = np.linspace(-5 * np.pi, 5 * np.pi, 512)  # 生成从-2π到2π的256个数据
cos, sin = np.cos(x), np.sin(3 * x)  # 分别计算x的cos和sin函数值
ax.set_xticks([i * np.pi for i in range(-5, 6)])  # 设置x轴的刻度
plt.plot(x, 2 * cos, color="blue", linewidth=2, linestyle="-", label="cos")  # 画出cos曲线，颜色为蓝色，线宽为2，连续线
plt.plot(x, sin, color="red", linewidth=2, linestyle="--", label="sin")  # 画出sin曲线，颜色为红色，线宽为2，间断线
# 画出十字形的坐标轴
ax.spines["right"].set_visible(False)  # 隐藏右边框
ax.spines["top"].set_visible(False)  # 隐藏上边框
ax.spines['bottom'].set_position(('data', 0))  # 设置下边框到y轴0的位置
ax.xaxis.set_ticks_position('bottom')  # 刻度值设置在下方
ax.spines['left'].set_position(('data', 0))  # 设置左边框到x轴0的位置
ax.yaxis.set_ticks_position('left')  # 刻度值设置在左侧
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('part1-4.png')
plt.show()
