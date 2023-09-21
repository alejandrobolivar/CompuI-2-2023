# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:05:40 2023

@author: bolivar
"""

from sympy import symbols, Eq, solve
from sympy.plotting import plot

# Definimos las variables x e y
x, y = symbols('x y')

# Definimos las ecuaciones
ecuacion1 = Eq(3*x + 2*y, 18)
ecuacion2 = Eq(5*x + 6*y, 18)

# Despejamos y
y_despejado1 = solve(ecuacion1, y)[0]
y_despejado2 = solve(ecuacion2, y)[0]

# Creamos la lista de funciones a graficar
funciones = [y_despejado1, y_despejado2]

# Graficamos todas las funciones juntas
plot(*funciones, (x, -10, 10))