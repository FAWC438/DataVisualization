import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

# 1.生成fig对象和ax对象
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 2.生成数据
x = np.random.randint(-100, 100, 100)  # x轴，生成100个在-100到100之间的整数
y = np.random.randint(-100, 100, 100)  # y轴，生成100个在-100到100之间的整数
z = np.random.randint(0, 20000, 100)  # z轴，生成100个在0到20000之间的整数
# 3.调用scatter，画3D散点图

ax.scatter(x, y, z, zdir='z', s=20, c=None, depthshade=True)

x1 = np.random.randint(-100, 100, 100)  # x轴，生成100个在-100到100之间的整数
y1 = np.random.randint(-100, 100, 100)  # y轴，生成100个在-100到100之间的整数
z1 = np.random.randint(0, 20000, 100)  # z轴，生成100个在0到20000之间的整数
ax.scatter(x1, y1, z1, zdir='z', s=20, c='r', marker='^', depthshade=True)

x2 = np.random.randint(-100, 100, 10000)  # x轴，生成5000个在-100到100之间的整数
y2 = np.random.randint(-100, 100, 10000)  # y轴，生成5000个在-100到100之间的整数
z2 = x2 ** 2 + y2 ** 2  # 生成z轴的数据
# z2 = x2**3+ y2**3                 #生成z轴的数据
ax.scatter(x2, y2, z2, zdir='z', s=20, c='g', marker='^', depthshade=True)

# 4.显示图形
plt.show()
