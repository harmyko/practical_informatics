#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:17:08 2024

@author: ugte0917
"""

import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-5, 5, 50001)

F1 = 1/(np.cbrt(X))
F2 = 1/X
F3 = 1/(X ** 2)

plt.plot(X, F1, linestyle="-", label=r"$f_1(x)=\frac{1}{\sqrt[3]{x}}$")
plt.plot(X, F2, linestyle="--", label=r"$f_2(x)=\frac{1}{x}$")
plt.plot(X, F3, linestyle=":", label=r"$f_3(x)=\frac{1}{x^2}$")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Hiperbolės")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
plt.close()