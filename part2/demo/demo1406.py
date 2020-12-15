import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# 读取数据
BasePath = 'c:\\code'  # cvs文件的保存路径
iris = pd.read_csv(BasePath + '\\iris.csv')
print(iris)
colors = ['r', 'y', 'b']  # 定义三种散点的颜色
Species = iris.Species.unique()  # 对类别去重
print(Species)

# 绘制散点图1
# plt.subplot(1,2,1)  #设置子图有2个，即1行2列，先画左边的第一个
'''
for i in range(len(Species)):
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Length'],
                iris.loc[iris.Species == Species[i], 'Petal.Width'], s = 35, c = colors[i], label = Species[i])
    # 添加轴标签和标题
    plt.title( 'Length vs Width')
    plt.xlabel( 'Petal.Length')
    plt.ylabel( 'Petal.Width')
    plt.grid(True, linestyle='--', alpha=0.8) #设置网格线
    plt.legend(loc = 'lower right') # 添加图例
    plt.show()
'''
plt.subplot(1, 2, 1)  # 设置子图有2个，即1行2列，先画左边的第一个
for i in range(len(Species)):
    print(iris.loc[iris.Species == Species[i], 'Petal.Length'])
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Length'],
                iris.loc[iris.Species == Species[i], 'Petal.Width'], s=35, c=colors[i], label=Species[i])
# 添加轴标签和标题
plt.title('Length vs Width')
plt.xlabel('Petal.Length')
plt.ylabel('Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8)  # 设置网格线
plt.legend(loc='lower right')  # 添加图例

# 绘制散点图2
plt.subplot(1, 2, 2)  # 设置子图有2个，即1行2列，再画右边的第二个
for i in range(len(Species)):  # x和y轴交换一下位置
    plt.scatter(iris.loc[iris.Species == Species[i], 'Petal.Width'],
                iris.loc[iris.Species == Species[i], 'Petal.Length'], s=35, c=colors[i], label=Species[i])
# 添加轴标签和标题
plt.title('Width vs Length')
plt.xlabel('Petal.Width')
plt.ylabel('Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8)  # 设置网格线
plt.legend(loc='lower right')  # 添加图例

plt.show()
