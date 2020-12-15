import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

# 1.生成fig对象和ax对象
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')
ax1.set_zlabel('Z Label')
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
ax2.set_zlabel('Z Label')

# 2.生成数据
x1 = np.array([0, 0, 0, 1, 1, 1])  # 生成x轴的数据
y1 = np.array([0, 1, 2, 0, 1, 2])  # 生成y轴的数据
z1 = x1 + y1  # 生成z轴的数据

# 3.调用plot，画3D的线图
ax1.plot(x1, y1, z1, "r", marker='o')

x2 = np.array([0, 1, 0, 1, 0, 1])  # 生成x轴的数据
y2 = np.array([0, 1, 2, 0, 1, 2])  # 生成y轴的数据
z2 = x2 + y2
# y2 = np.array([0,0,0,0,0,0])
# z2= np.array(np.arange(6))
ax2.plot(x2, y2, z2, "b", marker='o')

# 4.显示图形
plt.show()
