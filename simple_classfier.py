#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jiyu Li time:2018/4/16
#简单分类器实例

import numpy as np
import matplotlib.pyplot as plt
#1 构建原始数据
X = np.array([[3,1],[2,5],[1,8],[6,4],[5,2],[3,5],[4,7],[4,-1]])
y = [0,1,1,0,0,1,1,0]
#2 根据标签值分成两类
class_0 = np.array([X[i] for i in range(len(X)) if y[i] == 0])
class_1 = np.array([X[i] for i in range(len(X)) if y[i] == 1])
#线性分类器
line_x = range(10)
line_y = line_x

#绘图表示分类
plt.figure()
plt.scatter(class_0[:,0],class_0[:,1],color="black",marker="s")
plt.scatter(class_1[:,0],class_1[:,1],color="black",marker="x")
plt.plot(line_x,line_y,color="red",linewidth=3)
plt.show()

