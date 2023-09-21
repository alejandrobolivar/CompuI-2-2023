# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:43:07 2023

@author: bolivar


Dadas una ecuación con dos expresiones A=(Pu/2)+Mu/(lw-x)) y
 B=0.85*280*b*x, donde A=B y x es la incógnita. Determinar x
"""

import sympy as sym
x = sym.Symbol('x')
lw = 5.65    # largo muro
Pu = 258.7   # toneladas
Mu = 1.525   # tonelada-metro
Vu = 128     # tonelada
b = 0.3
resultado = sym.solve([sym.Eq(((Pu / 2) + Mu / (lw - x)), 0.85 * 280 * b * x)],x)
print(resultado)