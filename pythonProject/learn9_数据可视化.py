# import json
#
# data=[{"name":"老王","age":19},{"name":"张三","age":33}]
#
# json_str=json.dumps(data,ensure_ascii=False)#中文展示
#
# print(type(json_str))#将文件转换为json模式
#
# print(json_str)
#
# l=json.loads(json_str)#将文件由json模式转化回来
# print(l,type(l))
#json本质上来说就是有着特殊格式的字符串
from optparse import Option

from pyecharts import *
from pyecharts.types import VisualMap

line = charts.Line()

line.add_xaxis(["美国","中国","英国"])
line.add_yaxis("GDP",[60,100,30])

line.set_global_opts(
    title_opts=options.TitleOpts(True,"GDP展示",pos_left="center",pos_bottom="1%"),
     legend_opts=options.LegendOpts(is_show=True),
    toolbox_opts=options.ToolboxOpts(True),
    visualmap_opts=options.VisualMapOpts(True),
)



line.render()
#实战项目:物理实验数据折线图生成器