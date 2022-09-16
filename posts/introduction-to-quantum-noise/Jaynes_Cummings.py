#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:02:18 2022

@author: klucas
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as C

omega_r = 1e9
g = 0.01
delta = np.arange(-0.1,0.1,0.001)
n = 1

def Energy(n, omega_r, g, delta, p):
    #如果为+态, p=1；如果为-态，p=0或-1。
    if p==1:
        E = (delta/2 + np.sqrt(delta**2+4*n*g**2)/2)*1000
    elif p==0 or p==-1:
        E = (delta/2 - np.sqrt(delta**2+4*n*g**2)/2)*1000
    return E

fig, ax = plt.subplots(figsize=(8,6), dpi=200)
ax.plot(delta, Energy(n, omega_r, g, delta, 1))
ax.plot(delta, Energy(n, omega_r, g, delta, 0))
ax.plot(delta, (np.zeros(np.size(delta)))*1000, "g--")
ax.plot(delta, delta*1000, "g--")
ax.legend((r"$E_{+,1}/\hbar-\omega_r$", r"$E_{-,1}/\hbar-\omega_r$"), frameon = False)
ax.set_xlabel(r"$\Delta\ (Hz)$")
ax.set_ylabel(r"$E_{\pm,1}/\hbar-\omega_r\ (mHz)$")
plt.title("Jaynes-Cummings Model")
plt.show(fig)

# 导出图片
fig.savefig("Jaynes-Cummings.png")