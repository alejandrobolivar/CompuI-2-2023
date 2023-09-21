# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:54:23 2023

@author: bolivar
"""
from sympy import symbols, sin, pi
from sympy. plotting import plot3d
x, y = symbols ('x y')
plot3d (sin(x*y) ,(x,-pi/2,pi /2) ,(y,-pi/2,pi /2))