#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:13:29 2022

@author: cornelius
"""

import math

liste = [12,24,36,48,60,43]


def standard_deviation(data):
    mean = sum(data)/len(data)
    variance = sum((l-mean)**2 for l in data)/len(data)
    std = math.sqrt(variance)
    return std




print(standard_deviation(liste))







import numpy as np
print(np.std(liste))