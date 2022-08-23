#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:55:55 2022

@author: klucas
"""

from qutip import *
import numpy as np
import scipy.constants as C
import matplotlib.pyplot as plt

omega_q = 1e9
H = C.hbar / 2 * 1e12 * sigmaz()
psi0 = (basis(2, 1)+basis(2,0)).unit()
gamma_r = 0.01
gamma_phi = 0.01
times = np.linspace(0.0, 1000.0, 10000)
result = mesolve(H, psi0, times, 
                 [-np.sqrt(gamma_phi / 2)  * sigmaz()], 
                 [sigmaz(), sigmax(), num(2)])

fig, ax = plt.subplots(figsize=(8,6), dpi=200)
ax.plot(times, result.expect[0])
ax.plot(times, result.expect[1])
ax.plot(times, result.expect[2])
ax.set_xlabel('Time')
ax.set_ylabel('Expectation values')
plt.title("Dephasing")
ax.legend((r"$\langle\sigma_z\rangle$", 
           r"$\langle\sigma_x\rangle$", 
           r"$\langle n \rangle$"), frameon = False)
plt.show(fig)

# 导出图片
fig.savefig("Dephasing.png")