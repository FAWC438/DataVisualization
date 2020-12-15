import matplotlib.pyplot as plt
import numpy as np

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
count = 5

x = y = np.arange(count)
x1, y1 = np.meshgrid(x, y)
x1 = x1.flatten()  # 变为一维数组
y1 = y1.flatten()

z_list = np.array([[1, 2, 3, 4, 5],
                   [16, 17, 18, 19, 6],
                   [15, 24, 25, 20, 7],
                   [14, 23, 22, 21, 8],
                   [13, 12, 11, 10, 9]])
z = z_list.flatten()

bottom = np.zeros_like(z)  # 产生一个全零的矩阵，形状和z一样。bottom表示直方图从哪个数值开始是底部

width = depth = 0.5
ax.bar3d(x1, y1, bottom, width, depth, z, shade=True)

# 4.显示图形
ax.view_init(20, 320)  # 调整视角
plt.tight_layout()
plt.savefig('part2-5.png')
plt.show()
