#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jiyu Li time:2018/3/24
#数据预处理

import numpy as np
from sklearn import preprocessing
#构造原始数据
data = np.array([[3,-1.5,2,-5.4],[0,4,-0.3,2.1],[1,3.3,-1.9,-4.3]])

data_standard = preprocessing.scale(data)
data_mean = data_standard.mean(axis=0)  #特征值
data_std = data_standard.std(axis=0) #标准差
print "Mean=",data_mean
print "STD=",data_std
#范围缩放，讲原始数据缩放到合适范围
data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled = data_scaler.fit_transform(data)
print "\n Min max scale data:\n",data_scaled

#归一化
data_normalization = preprocessing.normalize(data,norm="l1")
print "\nnormalizated data\n",data_normalization

#二值化
data_binary = preprocessing.Binarizer(threshold=1.4).transform(data)
print "\nBinarized data\n",data_binary
#标记编码
label_encoder = preprocessing.LabelEncoder()
input_class = ['audi','ford','audi','toyato','ford','bmw']
label_encoder.fit(input_class)
print "\n 类地图"
for i,item in enumerate(label_encoder.classes_):
    print item,"-->",i

labels = ['audi','ford','toyato']
encoded_label1 = label_encoder.transform(labels)   #单词转数字
print "编码",list(encoded_label1)

encoded_label2 = [2,1,0,3,1]
decode_labels = label_encoder.inverse_transform(encoded_label2) #数字转单词
print "解码",list(decode_labels)