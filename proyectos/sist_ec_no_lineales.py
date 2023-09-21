# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 20:13:46 2023

@author: bolivar

sistema de ecuaciones no lineales 

"""

from sympy import var, solve

x, y = var('x y')

f1 = (x**2)+(y**2)-2*(4.41*x+2.68*y)+25.59
f2 = (x**2)+(y**2)-2*(3.23*x+2.1*y)+14.49

sols = solve((f1, f2), (x, y))