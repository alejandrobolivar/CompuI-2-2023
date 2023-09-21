# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:13:59 2023

@author: bolivar

Calcular el volumen del sólido de revolución generado cuando la región acotada
 por la curva y=x^2, el eje x y las rectas x=1 y x=2 se gira alrededor
 del eje x
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

u = np.linspace(-1, 2, 60)
v = np.linspace(0, 2*np.pi, 60)
U, V = np.meshgrid(u, v)

X = U
Y1 = (U**2 + 1) * np.cos(V)
Z1 = (U**2 + 1) * np.sin(V)

Y2 = (U + 3) * np.cos(V)
Z2 = (U + 3) * np.sin(V)

ax.plot_surface(X, Y1, Z1, alpha=0.3, color='red', rstride=6, cstride=12)
ax.plot_surface(X, Y2, Z2, alpha=0.3, color='blue', rstride=6, cstride=12)
plt.show()