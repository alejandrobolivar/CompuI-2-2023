# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:20:07 2023

@author: bolivar


suma de Riemann
suma izquierda

"""

import numpy as np
import matplotlib.pyplot as plt


def riemannplot(f, a, b, ra, rb, n):
    # f es la función 
    # a y b son los limites del eje x para graficar la funcion f
    # ra y rb son los limites del intervalo en el eje x del que queremos calcular la suma
    # n es el numero de rectangulos que calcularemos

    atenuacion = (b-a)/100
    x = np.arange(a, b+atenuacion, atenuacion)
    plt.plot(x, f(x), color='green')

    delta_x = (rb-ra)/n
    riemannx = np.arange(ra, rb, delta_x)
    riemanny = f(riemannx)
    riemann_sum = sum(riemanny*delta_x)

    plt.bar(riemannx,riemanny,width=delta_x,alpha=0.5,facecolor='orange')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Suma izquierda de Riemann para f(x)')
    plt.figtext(0.1,0.02, "Suma de Riemann: " + str(riemann_sum), color='r')
    plt.show()


def f(x):
    return x**2

riemannplot(f, 0, 1.1, 0, 1, 7)