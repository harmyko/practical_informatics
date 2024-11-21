#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 20:17:08 2024

@author: ugte0917
"""

import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-5, 5, 5000)
F1 = 1/(np.cbrt(X))
plt.plot(X, F1, linestyle="-", label=r"$f_1(x)=\frac{1}{sqrt[3]{x}}$")
plt.show()
plt.close()