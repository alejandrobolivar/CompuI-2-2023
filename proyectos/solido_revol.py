# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:48:47 2023

@author: bolivar

El volumen de un sólido de revolución generado al rotar la región delimitada
 por las curvas y=f(x), y=g(x) (donde f(x) y g(x) son funciones de x)
 sobre el eje x es dado por:

V = pi * ∫[a,b] (f(x)^2 - g(x)^2) dx

En donde a y b son los limites de la region.

Calcule el volumen del sólido generado al girar sobre el eje OY la región
 limitada por las curvas x = ((5)**1/2)y**2 , x = 0, y = −1, y = 1.

"""
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

y = sy.symbols('y')

def f(y):
    return (5**(1/2)) * y**2

def g(y):
    return 0

a, b = -1, 1

x1 = np.linspace(a, b, 200)
y1 = [f(y) for y in x1]

x2 = np.linspace(a, b, 200)
y2 = [g(y) for y in x2]

fig, ax = plt.subplots(figsize=(10,8))

ax.plot(x1, y1)
ax.plot(x2, y2)

plt.show()

volumen = sy.N(sy.pi * sy.integrate((f(y)**2 - g(y)**2), (y, a, b)))
print(f'Volumen= {volumen:.2f}')