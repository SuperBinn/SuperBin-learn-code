#!/usr/bin/env python
# coding: utf-8

# # 柱形图：标题，主题颜色，工具箱，左拉右拉功能，设置平均线等功能

# In[44]:


from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar

v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]

bar = (
    
    Bar(opts.InitOpts(width = '800px',height = '300px',theme=ThemeType.DARK))
    .add_xaxis(x)
    .add_yaxis("商家A", v1)
    .add_yaxis("商家B", v2)
    
    .set_global_opts(
               title_opts={"text": "商场数据显示"},
               xaxis_opts= opts.AxisOpts(
                      splitline_opts=opts.SplitLineOpts(is_show=True)
                ),  # 设置x轴  便于对齐旁边的数字
            yaxis_opts= opts.AxisOpts(
                      splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1))
                ),  # 设置y轴  便于对齐旁边的数字
            toolbox_opts = opts.ToolboxOpts(is_show = True),  # 设置工具箱，提供下载等等工具
            datazoom_opts= [opts.DataZoomOpts(range_start=10, range_end=80,is_zoom_lock=False)]     #左拉右拉功能         
                    )
    
     .set_series_opts(
            # 设置系列配置
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="average", name="平均值"),
                ]
            ),
        )
    )

bar.render_notebook()


# # 折线图:is_smooth可以使折线变成圆滑曲线  
# 
# is_step可以使折线变成阶梯曲线
#                        

# In[43]:


from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Line

v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]

line=(
Line(opts.InitOpts(width="500px",height="400px") ) 
.add_xaxis(x)
.add_yaxis("商品a",v1,is_smooth=True)
.add_yaxis("商品b",v2,is_step=True)
     )

line.render_notebook()


# # 绘制散点图Scatter

# In[46]:


from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Scatter

v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]

sca1=(
Scatter(opts.InitOpts(width="500px",height="400px") ) 
.add_xaxis(x)
.add_yaxis("商品a",v1)
.add_yaxis("商品b",v2)
     )

sca1.render_notebook()


# In[ ]:




