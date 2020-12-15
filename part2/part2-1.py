import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率

fig, ax = plt.subplots(nrows=4, ncols=4, figsize=(13, 13))
# 读取数据
iris = pd.read_csv('iris.csv')
# print(iris)
colors = ['skyblue', 'orange', 'g']  # 定义三种散点的颜色
Species = iris.Species.unique()  # 对类别去重
# print(Species)
data_type = ['Sepal.length', 'Sepal.width', 'Petal.Length', 'Petal.Width']

for j in range(4):
    for k in range(4):
        # 绘制散点图
        for i in range(len(Species)):
            print(iris.loc[iris.Species == Species[i], data_type[j]])
            ax[j, k].scatter(iris.loc[iris.Species == Species[i], data_type[j]],
                             iris.loc[iris.Species == Species[i], data_type[k]], s=35, c=colors[i], label=Species[i])
        # 添加轴标签和标题
        ax[j, k].set_title(data_type[j] + ' vs ' + data_type[k])
        ax[j, k].set_xlabel(data_type[j])
        ax[j, k].set_ylabel(data_type[k])
        ax[j, k].grid(True, linestyle='--', alpha=0.8)  # 设置网格线

ha, lb = ax[0, 0].get_legend_handles_labels()
plt.figlegend(ha, lb, loc='center right', fontsize=15)  # 添加图例
plt.tight_layout()
plt.subplots_adjust(right=0.8)
plt.savefig('part2-1.png')
plt.show()
