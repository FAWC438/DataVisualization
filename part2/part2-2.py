import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
通过北京2015年PM密度的CSV数据作饼图

0-50 Ⅰ 优
51-100 Ⅱ 良
101-150 Ⅲ 轻度污染
151-200 Ⅳ 中度污染
201-300 Ⅴ 重度污染
>300 Ⅵ 严重污染
'''

df = pd.read_csv('Cities_PM_2015.csv', encoding='utf-8')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率
sections = [0, 50, 100, 150, 200, 300, np.inf]  # 划分为不同长度的区间

pollution_level = ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']
explode = [0, 0, 0.1, 0.1, 0.1, 0.1]

# 按空气质量区间分割
result = pd.cut(df['Beijing'], sections, labels=pollution_level)
pollution_count = pd.value_counts(result, sort=False)  # 得到各部分的数量

# 若无某个等级的数据则将该等级在图中删除，同时需要同步更新标签和饼图样式
pollution_count_copy = pollution_count.copy()
pollution_level_copy = pollution_level.copy()
explode_copy = explode.copy()
for i in range(len(pollution_count_copy)):
    if pollution_count_copy[i] == 0:
        pollution_level.remove(pollution_level_copy[i])
        explode.remove(explode_copy[i])
pollution_count = pollution_count[0 != pollution_count.values]

for i in range(len(pollution_level)):
    pollution_level[i] += (': ' + str(pollution_count[i]) + '天')

patches, l_text, p_text = plt.pie(pollution_count, startangle=90, explode=explode, labels=pollution_level,
                                  autopct='%1.2f%%', labeldistance=1, textprops={'fontsize': 10, 'color': 'black'})
plt.title('2015年北京空气质量分级天数占比图')
plt.axis('equal')
# 图例
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('Beijing2015PM.png')
plt.show()
