import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data1402.csv', encoding='utf-8', header=None, names=['Score'])
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率

sections = [i for i in range(101) if i % 5 == 0]
label = [sections[i + 1] for i in range(len(sections) - 1)]

result = pd.cut(df['Score'], sections, labels=label)
student_count = pd.value_counts(result, sort=False)  # 得到各部分的数量

student_count_drop_zero = student_count.drop(student_count[student_count == 0].keys())
print(student_count_drop_zero)
print(student_count_drop_zero.describe())
print(student_count_drop_zero.values)
plt.axis([50, 100, 0, 30])  # 设置x轴和y轴的最小和最大值
plt.bar(student_count_drop_zero.keys(), student_count_drop_zero, 2, alpha=0.5, color='b')
plt.xlim(student_count_drop_zero.keys()[0] - 5, student_count_drop_zero.keys()[-1] + 5)
plt.ylim(0, student_count_drop_zero.max() + 5)
plt.xticks(student_count_drop_zero.keys(),
           [str(item - 5) + ' - ' + str(item) for item in student_count_drop_zero.keys()])
for a, b in zip(student_count_drop_zero.keys(), student_count_drop_zero):  # 在直方图上显示数字
    plt.text(a, b + 0.2, '%d' % b, ha='center', va='bottom', fontsize=8, color='black')

plt.title('成绩数据分段统计')
plt.xlabel("成绩分数段")
plt.ylabel("人数")
# 绘制直方图，第三个参数表示直方图的宽度，alpha为透明度,color为颜色
plt.tight_layout()
plt.savefig('part1-2.png')
plt.show()
