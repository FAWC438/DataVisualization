import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

df = pd.read_csv('中国大学数量.csv', encoding='utf-8', skiprows=[0, 1],
                 names=['Province', '2017_population', '2016_population', '211_985_num', 'Public_undergraduate_num'])


# print(type(df.at[0, '2017_population']))
# print(df.at[0, '2017_population'])
# print(len(df))
# print(df.at[0, '2017_population'][:-1])
# print(type(df.at[0, '211_985_num']))
# print(df.at[0, '211_985_num'])


class Data:
    provinces = df['Province'].to_list()

    @staticmethod
    def values_2017_population() -> list:
        return [float(df.at[i, '2017_population'][:-1]) for i in range(len(df))]

    @staticmethod
    def values_2016_population() -> list:
        return [float(df.at[i, '2016_population'][:-1]) for i in range(len(df))]

    @staticmethod
    def values_211_985_num() -> list:
        return [int(df.at[i, '211_985_num']) for i in range(len(df))]

    @staticmethod
    def values_Public_undergraduate_num() -> list:
        return [int(df.at[i, 'Public_undergraduate_num']) for i in range(len(df))]


def map_universityNum() -> Map:
    c = (
        Map()
            .add("各省211与985大学数量", [list(z) for z in zip(Data.provinces, Data.values_211_985_num())], "china",
                 selected_mode='single')
            .add("各省公办本科大学数量", [list(z) for z in zip(Data.provinces, Data.values_Public_undergraduate_num())], "china",
                 is_selected=False, selected_mode='single')
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=0, max_=60),
                             legend_opts=opts.LegendOpts(selected_mode="single"))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


def map_population() -> Map:
    c = (
        Map()
            .add("各省2017年高考人数（单位：万人）", [list(z) for z in zip(Data.provinces, Data.values_2017_population())], "china",
                 selected_mode='single')
            .add("各省2016年高考人数（单位：万人）", [list(z) for z in zip(Data.provinces, Data.values_2016_population())], "china",
                 selected_mode='single', is_selected=False)
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=0, max_=100),
                             legend_opts=opts.LegendOpts(selected_mode="single"))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


map_universityNum().render("MapUniversityNumber.html")
map_population().render("MapPopulation.html")
print("done")
