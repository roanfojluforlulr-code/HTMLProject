# 导包
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
# 美国
f_US = open("C:/Pycharm/美国.txt", 'r', encoding="UTF-8")
US_data = f_US.read()
# 日本
f_JP = open("C:/Pycharm/日本.txt", 'r', encoding="UTF-8")
JP_data = f_JP.read()
# 印度
f_IN = open("C:/Pycharm/印度.txt", 'r', encoding="UTF-8")
IN_data = f_IN.read()

US_data = US_data.replace("jsonp_1629344292311_69436(", "")
JP_data = JP_data.replace("jsonp_1629350871167_29498(", "")
IN_data = IN_data.replace("jsonp_1629350745930_63180(", "")

US_data = US_data[:-2]
JP_data = JP_data[:-2]
IN_data = IN_data[:-2]

US_dict = json.loads(US_data)
JP_dict = json.loads(JP_data)
IN_dict = json.loads(IN_data)

# 获取trend key
US_trend_data =  US_dict['data'][0]['trend']
JP_trend_data =  JP_dict['data'][0]['trend']
IN_trend_data =  IN_dict['data'][0]['trend']

# 获取x轴(日期数据) 取2020年的
US_x_data = US_trend_data['updateDate'][:314]
JP_x_data = JP_trend_data['updateDate'][:314]
IN_x_data = IN_trend_data['updateDate'][:314]

# 获取y轴(确认数据) 同样是2020年的
US_y_data = US_trend_data['list'][0]['data'][:314]
JP_y_data = JP_trend_data['list'][0]['data'][:314]
IN_y_data = IN_trend_data['list'][0]['data'][:314]

# 构建图表
line = Line()# 构建图表对象

# x轴共用
line.add_xaxis(US_x_data)

# y轴
line.add_yaxis("美国确诊人数", US_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", JP_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", IN_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    # 标题设计
    title_opts=TitleOpts(title="2020年美日印三国确诊人数", pos_left='center', pos_bottom='1%')
)

# 生成图表
line.render()

# 关闭文件
f_US.close()
f_JP.close()
f_IN.close()