import matplotlib.pyplot as mp # 数据可视化
# import pandas as pd # 序列高级函数
# import scipy as sc # 科学计算
import numpy as np # 基础值算法

# 进行线性拆分1000个点

x = np.linspace(-np.pi,np.pi,1000)
print(x,x.shape)



sinx = np.sin(x)
cosx = np.cos(x)
# 绘制余弦曲线 cos(x)/2
cosx = np.cos(x) / 2

# 设置坐标轴的范围
# mp.xlim(0,np.pi)
# mp.ylim(0,1)

# x/y轴 值列表 文本列表
# -π,-π/2,0,π/2,π
# frac{}{} 分数 {分子}{分母}
vals=[-np.pi,-np.pi/2,0, np.pi/2,np.pi]
 #1 texts=['-π','-π/2','0','π/2','π']
texts=[r'$-\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$-\pi$']
mp.xticks(vals,texts)

# 修改坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

mp.yticks([-1.0,-0.5,0.5,1.0])

# 线的样式，粗细，颜色,标签
mp.plot(x,sinx, linestyle = '--', linewidth=2, color='orangered', alpha=0.8,label=r'$y=sin(x)$')
mp.plot(x,cosx, linestyle ='-.', linewidth=2, color='dodgerblue', alpha = 0.9,label=r'$y=\frac{1}{2}cos(x)$')

# 绘制特殊点
pointx = [np.pi/2,np.pi/2]
pointy =[1,0]
mp.scatter(pointx,pointy,
           marker='o',s=70,color='red',
           label = 'sample points',zorder=3) # 图层优先度zorder

# 图例
mp.legend()
mp.show()

