from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
import random
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot


class Data:
    guangdong_city = ["佛山市", "湛江市", "潮州市", "河源市", "江门市", "中山市", "珠海市", "深圳市", "东莞市", "韶关市", "清远市", "云浮市", "茂名市", "汕头市",
                      "汕尾市", "揭阳市", "阳江市", "肇庆市", "广州市", "惠州市", "梅州市"]

    def values(self: int = 30, end: int = 40) -> list:
        return [random.randint(self, end) for _ in range(21)]


def geo_guangdong(title) -> Geo:
    c = (
        Geo()
            .add_schema(maptype="广东")
            .add(
            title,
            [list(z) for z in zip(Data.guangdong_city, Data.values())],
            type_=ChartType.HEATMAP,
        )
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=42),  # is_piecewise=True),
            title_opts=opts.TitleOpts(title="广东省8月份各地市温度变化情况"),
        )
    )
    return c


for i in range(5):
    str_date = "8月" + str(i + 1) + "日"
    make_snapshot(snapshot, geo_guangdong(str_date).render(),
                  str(i + 1) + ".png", pixel_ratio=1)
