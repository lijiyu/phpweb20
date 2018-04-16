#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jiyu Li time:2018/3/31

#3Dscatter 绘图

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#生成数据
n = 250
f = lambda minval,maxval,n:minval + (maxval-minval) * np.random.rand(n)
x_val = f(14,41,n)
y_val = f(-10,70,n)
z_val = f(-52,-37,n)

ax.scatter(x_val,y_val,z_val,c='k',marker='o')
#设置坐标轴标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#显示图
plt.show()
