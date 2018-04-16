#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jiyu Li time:2018/3/31
#饼图绘制

import numpy as np
import matplotlib.pyplot as plt
data = {'Apple':26,
        'Mango':17,
        'Pineapple':21,
        'Banana':29,
        'Strawberry':11}

colors = ['orange','lightgreen','lightblue','gold','cyan']

explode = (0,0,0,0,0)
plt.pie(data.values(),explode=explode,labels=data.keys(),colors=colors,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
