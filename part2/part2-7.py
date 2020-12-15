import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率

# 1.生成fig对象和ax对象
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 2.生成数据

x2 = np.random.randint(-100, 100, 1000)  # x轴，生成1000个在-100到100之间的整数
y2 = np.random.randint(-100, 100, 1000)  # y轴，生成1000个在-100到100之间的整数
z2 = x2 ** 2 + y2 ** 2 - 20000  # 生成z轴的数据
z3 = -x2 ** 2 - y2 ** 2 + 20000  # 生成z轴的数据
ax.scatter(x2, y2, z2, zdir='z', s=20, c='r', marker='^', depthshade=True)
ax.scatter(x2, y2, z3, zdir='z', s=20, c='skyblue', marker='^', depthshade=True)

# 4.显示图形
ax.view_init(2, 30)  # 调整视角
plt.tight_layout()
plt.savefig('part2-7.png')
plt.show()
