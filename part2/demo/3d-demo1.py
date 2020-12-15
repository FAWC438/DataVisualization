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
# x = np.array([0, 0, 0, 1, 1, 1])  # 生成x轴的数据
# y = np.array([0, 1, 2, 0, 1, 2])  # 生成y轴的数据
# z = x + y  # 生成z轴的数据
# print('=========================================z')
# print(type(z))
#
# x = np.array([0, 0, 0, 0, 1, 1, 1, 1])  # 生成x轴的数据
# y = np.array([0, 1, 2, 3, 0, 1, 2, 3])  # 生成y轴的数据
# z = np.array([5, 4, 2, 3, 2, 2, 0, 2])  # 生成z轴的数据

count = 50

x1 = a = np.zeros(count)
for i in range(count - 1):
    a = a + 1
    x1 = np.append(x1, a)
    # print(a)
print(x1)

y1 = b = np.arange(count)
for i in range(count - 1):
    y1 = np.append(y1, b)
    print(b)
print(y1)

z = x1 + y1  # 生成z轴的数据

print('=========================================bottom')
bottom = np.zeros_like(z)  # 产生一个全零的矩阵，形状和z一样。bottom表示直方图从哪个数值开始是底部
# bottom = z
print(bottom)

width = depth = 0.5  # width和depth表示直方柱的宽度和深度在单元格中比例
# 3.调用bar3d，画3D直方图
# ax.bar3d(x, y, bottom, width, depth, z, shade=True,color='r')
ax.bar3d(x1, y1, bottom, width, depth, z, shade=True)

# ax.set_xticklabels(["ICPC", "CCPC"])
# ax.set_xticks([0, 1])
# ax.set_yticklabels(["2016", "2017", "2018", "2019"])
# ax.set_yticks([0, 1, 2, 3])

# 4.显示图形
plt.show()
