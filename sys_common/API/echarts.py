import json
from random import randrange

from django.http import HttpResponse
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Map, WordCloud
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType


def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def echarts_pie(types: list, data: list, title: str) -> Pie:
    """
    画饼图
    :param types: list  分类
    :param data: list  数据
    :param title: str 标题
    """
    # types = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子', '其他']
    # data = [randrange(0, 100) for _ in range(7)]
    c = (
        Pie(
            init_opts=opts.InitOpts(theme=ThemeType.LIGHT, bg_color="#ffffff")
        )  # bg eef2f7
        .add(
            "",
            [list(z) for z in zip(types, data)],
            radius=["0%", "70%"],
            center=["50%", "50%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            legend_opts=opts.LegendOpts(
                is_show=True, orient="vertical", pos_left="1", pos_top="20%"
            ),
            visualmap_opts=(opts.VisualMapOpts(is_show=True, is_calculable=True)),
            toolbox_opts=opts.ToolboxOpts(
                orient="vertical", pos_left="right", pos_top="middle"
            ),
            brush_opts=opts.BrushOpts(tool_box=["clear"]),
            tooltip_opts=opts.TooltipOpts(
                trigger="item",
                trigger_on="mousemove",
                hide_delay=1000,
                background_color="green",
                border_color="#ccc",
                border_width=1,
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .dump_options_with_quotes()
    )
    return c


def echarts_bar() -> Bar:
    types = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    x_data = [randrange(0, 100) for _ in range(6)]
    y_data = [randrange(0, 100) for _ in range(6)]
    c = (
        Bar()
        .add_xaxis(types)
        .add_yaxis("商家A", x_data)
        .add_yaxis("商家B", y_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题")
        )
    )
    return c.dump_options_with_quotes()


def echarts_wordcloud(data):
    c = (
        WordCloud()
        .add(series_name="关键词分析", data_pair=data, word_size_range=[6, 66])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="关键词-热点分布",
                title_textstyle_opts=opts.TextStyleOpts(font_size=23),
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c.dump_options_with_quotes()


def echarts_map_china():
    provice = ["湖南", "湖北", "广东", "广西"]
    data = [randrange(0, 100) for _ in range(4)]
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.CHALK))  # CHALK
        .add("CHINA", [list(z) for z in zip(provice, data)], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-CHINA"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    return c.dump_options_with_quotes()


def echarts_map_world():
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.country, Faker.values())], "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-世界地图"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    return c.dump_options_with_quotes()


def echarts_map_gd():
    city = Faker.guangdong_city
    value = Faker.values()
    print(city, value)
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add("商家A", [list(z) for z in zip(city, value)], "广东")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="广东地图"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c.dump_options_with_quotes()
