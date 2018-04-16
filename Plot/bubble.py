#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jiyu Li time:2018/3/31
import numpy as np
import matplotlib.pyplot as plt

num_val = 40
x = np.random.rand(num_val)
y = np.random.rand(num_val)
max_radius = 25
area = np.pi * (max_radius*np.random.rand(num_val)) ** 2
color =  np.random.rand(num_val)
plt.scatter(x,y,s=area,c=color,alpha = 1.0)
plt.show()

