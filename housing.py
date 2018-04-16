#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jiyu Li time:2018/4/16

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn import datasets
from sklearn.metrics import mean_squared_error,explained_variance_score
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

housing_data = datasets.load_boston()
