# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:58:09 2023

@author: bolivar

trazar la siguiente curva 3D
alpha(t) = (cos(t), sin(t), t)
"""

from sympy import symbols, sin, cos
from sympy.plotting import plot3d_parametric_line

t = symbols('t')
alpha = [cos(t), sin(t), t]
plot3d_parametric_line(*alpha)
# También puede escribir:
# plot3d_parametric_line(cos(t), sin(t), t, (t, 0, 2*pi)) 
# en caso de definir limites a t.