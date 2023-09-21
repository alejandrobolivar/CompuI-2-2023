# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:09:23 2023

@author: bolivar
"""

import numpy as np
import matplotlib.pyplot as plt


np.seterr(divide='ignore', invalid='ignore')

fig = plt.figure()
solido = fig.add_subplot(111, projection='3d')

x  = np.linspace(0, 2, 100)
xRecta = np.linspace(0, 1.3, 100)    ### Intervalos de los segmentos de curva que
xParabola = np.linspace(1.3, 2, 100) ### delimitan el área. x = 1.3 intersección

para = -x**2 + 4  ### Funciones para dibujar la gráfica 2D
rect = x + 1

v = np.linspace(0, 2*np.pi, 100)

Xr, V = np.meshgrid(xRecta, v)
Yr = (Xr + 1) * np.cos(V)
Zr = (Xr + 1) * np.sin(V)

Xp, V = np.meshgrid(xParabola, v)
Yp = (-Xp**2 + 4) * np.cos(V)
Zp = (-Xp**2 + 4) * np.sin(V)

X = np.concatenate((Xr, Xp), axis=0)
Y = np.concatenate((Yr, Yp), axis=0)
Z = np.concatenate((Zr, Zp), axis=0)

solido.set(xlabel='x', 
       ylabel='y', 
       zlabel='z',
       xlim = [0, 2],
       ylim = [-3, 3],
       zlim = [-3, 3],
       title='Sólido de revolución')

grafica = fig.add_axes([0.05,0.7,0.15,.2])
grafica = plt.plot(x, para, 'r')
grafica = plt.plot(x, rect, 'b')

solido.plot_surface(X, Y, Z, cmap='viridis')

plt.show()
