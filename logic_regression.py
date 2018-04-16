#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jiyu Li time:2018/4/16
#逻辑分类器

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

#分类数据集合
X = np.array([[4,7],[3.5,8],[3.1,6.2],[0.5,1],[1,2],[1.2,1.9],[6,2],[5.7,1.5],[5.4,2.2]])
y = np.array([0,0,0,1,1,1,2,2,2])
#创建分类器
classifier = linear_model.LogisticRegression(solver='liblinear',C=100)
#训练分类器
classifier.fit(X,y)

def plot_classifier(classifier,X,y):
    x_min,x_max = min(X[:,0])-1.0,max(X[:,0])+1.0
    y_min, y_max = min(X[:,1]) - 1.0, max(X[:,1]) + 1.0
    #定义网格
    step_size = 0.01
    x_values,y_values = np.meshgrid(np.arange(x_min,x_max,step_size),np.arange(y_min,y_max,step_size))
    #计算分类器输出结果
    mesh_output = classifier.predict(np.c_[x_values.ravel(),y_values.ravel()])
    mesh_output = mesh_output.reshape(x_values.shape)
    plt.figure()
    #选择配色方案
    plt.pcolormesh(x_values,y_values,mesh_output,cmap=plt.cm.gray)
    plt.scatter(X[:,0],X[:,1],c=y,s=80,edgecolors="black",linewidths=1,cmap=plt.cm.Paired)
    #设置图像取值范围
    plt.xlim(x_values.min(),x_values.max())
    plt.ylim(y_values.min(), y_values.max())
    #设置坐标轴
    plt.xticks((np.arange(int(min(X[:,0])-1), int(max(X[:,0])+1),1.0)))
    plt.yticks((np.arange(int(min(X[:, 1]) -1), int(max(X[:, 1]) + 1), 1.0)))
    plt.show()

#画出图像
plot_classifier(classifier,X,y)
