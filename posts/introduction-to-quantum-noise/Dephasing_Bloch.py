#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:45:12 2022

@author: klucas
"""

from qutip import *
import numpy as np

b = Bloch()
gamma_r = 0.1
t_m = 10

b.point_color=['k']
b.point_marker=['.']

for t in range(20):
    a = Qobj([[1-np.exp(-gamma_r*t),0],[0,np.exp(-gamma_r*t)]])
    b.add_states(a, 'point')
    
b.show()