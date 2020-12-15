import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager as fm

# from matplotlib import cm

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# matplotlib.rcParams['axes.unicode_minus'] = False

label_list = ["出国", "保送外校读研", "本校硕博连读", "保送本校读研", "考研"]  # 各部分标签

size = [12, 7, 5, 10, 2]  # 各部分的人数
explode = [0.2, 0, 0, 0, 0]  # 各部分的突出显示比例

patches, texts, autotexts = \
    plt.pie(size, explode=explode, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=True, startangle=0,
            pctdistance=0.6)

proptease = fm.FontProperties()
proptease.set_size('xx-large')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(texts, fontproperties=proptease)
plt.setp(autotexts, fontproperties=proptease)

plt.show()

print(patches)
print(texts)
print(autotexts)
