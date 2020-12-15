import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率

# 1.生成fig对象和ax对象
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')
ax1.set_zlabel('Z Label')
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
ax2.set_zlabel('Z Label')

# 2.生成数据
x1 = np.array([0, 0, 5, 5, 2.5, 5, 0, 2.5, 0, 5])  # 生成x轴的数据
y1 = np.array([0, 5, 5, 0, 2.5, 5, 5, 2.5, 0, 0])  # 生成y轴的数据
z1 = np.array([0, 0, 0, 0, 5, 0, 0, 5, 0, 0])  # 生成z轴的数据

# 3.调用plot，画3D的线图
ax1.plot(x1, y1, z1, "r")

z2 = np.array([0, 0, 0, 0, -5, 0, 0, -5, 0, 0])  # 生成下方的z轴数据

ax2.plot(x1, y1, z2, "b")
ax2.plot(x1, y1, z1, "r")

# 4.显示图形
ax1.view_init(10, 30)  # 调整视角
ax2.view_init(10, 30)
plt.tight_layout()
plt.subplots_adjust(left=0.1)  # 调整标签位置
plt.savefig('part2-6.png')
plt.show()
