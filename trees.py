# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 11:08:34 2017
机器学习第二章、决策树



@author: Administrator
"""

from math import log
#计算香浓信息熵的函数，度量数据集的无序程度
def calcShannonEnt(dataSet):
    numEntries = len(dataSet) #总类别数
    labelCounts = {} #标签统计
    for featVec in dataSet:
        currentLabel = featVec[-1] #最后一列表示标签
        if currentLabel not in labelCounts.keys(): #当前标签不在标签集中
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
    shannonEnt =0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #信息熵
    return shannonEnt

#数据集合的产生
def createDataSet():
    dataSet = [[0,-1,'maybe'],
            [1,1,'yes'],
              [1,1,'yes'],
              [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels

#分割数据集函数
#参数1 dateSet 带划分的数据集
#参数2 axis 划分数据的特征
#参数3 特征的返回值
def splitDataSet(dataSet,axis,value):
    retDataSet = [] #常见list对象
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet




myData,lables = createDataSet()
s = calcShannonEnt(myData)
print(s)

                       