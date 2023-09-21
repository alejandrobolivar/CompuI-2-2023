# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:31:30 2023

@author: bolivar

trazar una superficie cuyas coordenadas z son una función de sus coordenadas
 x e y, debe crear una cuadrícula de todas las combinaciones posibles de
 coordenadas xy y obtener la cuadrícula z resultante.

"""

import matplotlib.pyplot as plt
import numpy as np

def z_func(x, y):
    z = 0.000855995633558468 * x ** 2 + 0.0102702516120239 * x + \
        0.00451027901725375 * y ** 2 - 2.23785431578513 * y + \
        251.029058292935
    return z

# Creates a 1D array of all possible x and y coordinates
x_coords = np.linspace(-30, 30, 100)
y_coords = np.linspace(180, 220, 100)

# Creates 2D array with all possible combinations of x and y coordinates,
# so x_grid.shape = (100, 100) and y_grid.shape = (100, 100)
[x_grid, y_grid] = np.meshgrid(x_coords, y_coords)

# Evaluates z at all grid points
z_grid = z_func(x_grid, y_grid)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid,y_grid,z_grid)
plt.show()