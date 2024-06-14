import matplotlib.pyplot as mp # 数据可视化
import pandas as pd # 序列高级函数
import scipy as sc # 科学计算
import numpy as np # 基础值算法


# xarray:<序列>水平坐标
# yarray:<序列>垂直坐标

x = np.array([1,2,3,4,5,6])
y = np.array([12,39,36,25,13,4])

# 绘制垂直线
mp.vlines(4,10,35)

# 绘制水平线
mp.hlines([10,20,30,40],[1,2,3,4],[2,3,4,5])

# 显示图
mp.plot(x,y)
mp.show() 


# -------------------------参考用--------------------------------------------
# 属性	值类型
# alpha	浮点值
# animated	[True / False]
# antialiased or aa	[True / False]
# clip_box	matplotlib.transform.Bbox 实例
# clip_on	[True / False]
# clip_path	Path 实例， Transform，以及Patch实例
# color or c	任何 matplotlib 颜色
# contains	命中测试函数
# dash_capstyle	['butt' / 'round' / 'projecting']
# dash_joinstyle	['miter' / 'round' / 'bevel']
# dashes	以点为单位的连接/断开墨水序列
# data	(np.array xdata, np.array ydata)
# figure	matplotlib.figure.Figure 实例
# label	任何字符串
# linestyle or ls	[ '-' / '--' / '-.' / ':' / 'steps' / ...]
# linewidth or lw	以点为单位的浮点值
# lod	[True / False]
# marker	[ '+' / ',' / '.' / '1' / '2' / '3' / '4' ]
# markeredgecolor or mec	任何 matplotlib 颜色
# markeredgewidth or mew	以点为单位的浮点值
# markerfacecolor or mfc	任何 matplotlib 颜色
# markersize or ms	浮点值
# markevery	[ None / 整数值 / (startind, stride) ]
# picker	用于交互式线条选择
# pickradius	线条的拾取选择半径
# solid_capstyle	['butt' / 'round' / 'projecting']
# solid_joinstyle	['miter' / 'round' / 'bevel']
# transform	matplotlib.transforms.Transform 实例
# visible	[True / False]
# xdata	np.array
# ydata	np.array
# zorder	任何数值
# ---------------------------------------------------------------------