import random
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pandas import DataFrame

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率

base_list = [j for j in range(10)]
list_data = []
for i in range(3):
    random.shuffle(base_list)
    list_data.append(base_list.copy())

# print(np.array(list_data).T)
df = DataFrame(np.array(list_data).T, columns=['第一学期', '第二学期', '第三学期'])

print(df)
print(df.info())

plt.subplot(1, 3, 1)
plt.bar(df['第一学期'].keys(), df['第一学期'], color='r')
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
plt.xlabel('学生序号')
plt.ylabel('排名')
plt.title('第一学期')

plt.subplot(1, 3, 2)
plt.bar(df['第二学期'].keys(), df['第二学期'], color='g')
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
plt.xlabel('学生序号')
plt.ylabel('排名')
plt.title('第二学期')

plt.subplot(1, 3, 3)
plt.bar(df['第三学期'].keys(), df['第三学期'], color='b')
ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
plt.xlabel('学生序号')
plt.ylabel('排名')
plt.title('第三学期')

plt.tight_layout()
plt.savefig('part1-3.png')
plt.show()
