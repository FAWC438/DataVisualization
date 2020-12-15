import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('Beijing_reduced_data.csv', encoding='utf-8')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率

df_every_year_month = DataFrame()

fig, ax = plt.subplots()

for i in range(2010, 2016):
    df_temp = df[df['year'] == i]
    df_every_year_month[str(i)] = df_temp.groupby('month').mean()['average']

print(df_every_year_month.head())
print(df_every_year_month.info())

ax.set_xticks([i for i in range(1, 13)])  # 设置x轴的刻度
plt.plot(df_every_year_month['2010'].keys(), df_every_year_month['2010'], color="blue", linewidth=3,
         label="2010年")
plt.plot(df_every_year_month['2011'].keys(), df_every_year_month['2011'], color="cyan", linewidth=3,
         label="2011年")
plt.plot(df_every_year_month['2012'].keys(), df_every_year_month['2012'], color="y", linewidth=3,
         label="2012年")
plt.plot(df_every_year_month['2013'].keys(), df_every_year_month['2013'], color="orange", linewidth=3,
         label="2013年")
plt.plot(df_every_year_month['2014'].keys(), df_every_year_month['2014'], color="black", linewidth=3,
         label="2014年")
plt.plot(df_every_year_month['2015'].keys(), df_every_year_month['2015'], color="r", linewidth=3,
         label="2015年")

plt.title('北京2010-2015年PM指数月平均数据的变化情况')
plt.xlabel('月份')
plt.ylabel('PM指数')

ax.spines["right"].set_visible(False)  # 隐藏右边框
ax.spines["top"].set_visible(False)  # 隐藏上边框
ax.xaxis.set_ticks_position('bottom')  # 刻度值设置在下方
ax.yaxis.set_ticks_position('left')  # 刻度值设置在左侧
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('part1-5.png')
plt.show()
