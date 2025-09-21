from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts,ToolboxOpts, VisualMapOpts  # 可配置选项

line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])
# 设置全局配置
line.set_global_opts( # 参数后面一定要加逗号
    title_opts = TitleOpts(title="GDP指数", pos_left = "center", pos_bottom="1%"),# 控制标题与它的位置
    legend_opts= LegendOpts(is_show=True),# 控制图例
    toolbox_opts= ToolboxOpts(is_show=True),#工具箱
    visualmap_opts= VisualMapOpts(is_show=True)# 视觉映射
    # control + p 查看可用全局配置
)

line.render()