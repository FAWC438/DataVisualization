from pyecharts import options as opts
from pyecharts.charts import Map
import random
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot


class Data:
    provinces = ["湖北", "广东", "北京", "上海", "江西", "河南", "浙江", "江苏",
                 "湖南", "广西", "山东", "陕西", "山西", "河北", "福建", "黑龙江",
                 "新疆", "西藏", "云南", "贵州", "四川", "台湾", "宁夏", "吉林",
                 "青海", "甘肃", "内蒙古", "重庆", "安徽", "天津", "海南", "辽宁"]

    @staticmethod
    def values(start: int = 20, end: int = 150) -> list:
        return [random.randint(start, end) for _ in range(32)]


def map_base() -> Map:
    c = (
        Map().add("各省大学数量", [list(z) for z in zip(Data.provinces, Data.values())], "china").set_global_opts(
            title_opts=opts.TitleOpts(title="Map-基本示例"))
    )
    return c


map_base().render("map1-1.html")
make_snapshot(snapshot, map_base().render(), "map1-1.png")
'''
def map_visualmap() -> Map:
    c = (
        Map()
        .add("各省大学数量", [list(z) for z in zip(Data.provinces, Data.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(min_=20,max_=150))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c

for i in range(5):
    map_visualmap().render("map"+str(i)+".html")
'''
print("done")
