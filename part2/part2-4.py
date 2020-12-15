import random

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot

# 数据来源 http://www.tianqihoubao.com/lishi/fujian.htm
df = pd.read_excel('tempData.xlsx')
print(df)
print(df.at[0, '2020.11.' + str(1)])


class Data:
    fujian_city = ["福州市", "厦门市", "莆田市", "三明市", "泉州市", "漳州市", "南平市", "龙岩市", "宁德市"]

    @staticmethod
    def values(day: int) -> list:
        return [float(df.at[j, '2020.11.' + str(day)]) for j in range(9)]


def geo_fujian(day: int) -> Geo:
    c = (
        Geo()
            .add_schema(maptype="福建")
            .add("11月" + str(day) + "日", [list(z) for z in zip(Data.fujian_city, Data.values(day))],
                 type_=ChartType.HEATMAP, )
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(min_=10, max_=30,
                                              range_text=["High", "Low"],
                                              is_calculable=True,
                                              range_color=["lightskyblue", "yellow", "orangered"]),
            title_opts=opts.TitleOpts(title="福建省2020年11月份前10日各地市温度变化情况"),
        )
    )
    return c


for i in range(10):
    make_snapshot(snapshot, geo_fujian(i + 1).render(), 'fujianTemperature/' + str(i + 1) + '.png', pixel_ratio=1)
    print('finish day ' + str(i))

print('done')
