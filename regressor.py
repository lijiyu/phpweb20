#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jiyu Li time:2018/3/25

import sys
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

import sklearn.metrics as sm
import cPickle as pickle



#读取数据函数
def openfile(filename):
    x = []
    y = []
    with open(filename,'r') as f:
        for line in f.readlines():
            xt,yt = [float(i) for i in line.split(',')]
            x.append(xt)
            y.append(yt)
    return x,y

def run():
    X,Y = openfile("data.txt")
    num_training = int(0.8*len(X))  #训练数据集个数
    num_test = len(X) - num_training  #测试数据集个数
    #训练数据
    X_train = np.array(X[:num_training]).reshape((num_training,1))
    Y_train = np.array(Y[:num_training])
    #测试数据
    X_test = np.array(X[num_training:]).reshape((num_test,1))
    Y_test = np.array(X[num_training:])

    linear_regressor = linear_model.LinearRegression() #创建线性回归模型
    linear_regressor.fit(X_train,Y_train)  #训练线性模型

    y_train_pred = linear_regressor.predict(X_train)  #预测值
    y_test_pred = linear_regressor.predict(X_test) #预测测试结果集
    return y_test_pred,y_train_pred


def fig(X_train,Y_train,,y_train_pred,X_test,Y_test,y_test_pred):
    plt.figure()
    plt.scatter(X_train,Y_train,color="green")
    plt.plot(X_train,y_train_pred,color="black",linewidth=2)
    #测试集合
    plt.scatter(X_test,Y_test,color="blue")
    plt.plot(X_test,y_test_pred,color="red",linewidth=3)
    plt.title('Train Test')
    plt.show()

def evulate(x_test,y_test,y_test_pred):
    print "平均绝对偏差:",round(sm.mean_absolute_error(x_test,y_test_pred),2)
    print "均方误差:",round(sm.mean_squared_error(x_test,y_test_pred),2)
    print "中位数绝对误差",round(sm.median_absolute_error(y_test,y_test_pred),2)
    print "解释方位差",round(sm.explained_variance_score(y_test,y_test_pred),2)
    print "R2",round(sm.r2_score(y_test,y_test_pred))