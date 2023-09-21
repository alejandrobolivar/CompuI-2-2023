# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:08:08 2023

@author: bolivar
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

root = np.roots([1, 1, -3])[1] # punto de interseccion entre las curvas

r1 = np.linspace(0, root, 60)
r2 = np.linspace(root, 2, 60)

theta = np.linspace(0, 2*np.pi, 60)
R1, Theta = np.meshgrid(r1, theta)
R2, Theta = np.meshgrid(r2, theta)

X1 = np.append(R1, R2,  axis=0)
Y1 = np.append((-R1**2 + 4)*np.cos(Theta), (R2 + 1)*np.cos(Theta), axis=0)
Z1 = np.append((-R1**2 + 4)*np.sin(Theta), (R2 + 1)*np.sin(Theta), axis=0)

X2 = np.append(R1, R2,  axis=0)
Y2 = np.append((R1 + 1)*np.cos(Theta), (-R2**2 + 4)*np.cos(Theta), axis=0)
Z2 = np.append((R1 + 1)*np.sin(Theta), (-R2**2 + 4)*np.sin(Theta), axis=0)

ax.plot_surface(X1, Y1, Z1, alpha=0.3, color='blue', linewidth=0, antialiased=False)
ax.plot_surface(X2, Y2, Z2, alpha=0.3, color='green', linewidth=0, antialiased=False)

plt.show()